package O2DBI;

#
# $Id: O2DBI.pm,v 1.24 2000/12/04 09:26:55 jc Exp $
#
# create a database description and Perl modules to interface the database
# from an abstract description
#

($VERSION) = ('$Revision: 1.24 $' =~ /([\d\.]+)/g);

#use Data::Dumper;

# this hash contains the complete relational scheme of the database
%tables = ();

1;


sub deploy {
    my ($class, $schemeref, $basename, $backend) = @_;
    my %scheme = %$schemeref;

    # create a relational scheme from the object oriented description
    foreach $object (keys(%scheme)) {
	$tables{$object}{cols}{'id'} = 'pkey';
	# distinguish first and second class tables
	$tables{$object}{type} = '1';
	mktable($object, $scheme{$object}->{members});
	if ($scheme{$object}->{creator}) {
	    foreach $var (@{$scheme{$object}->{creator}}) {
		my ($array, $name) = ($var =~ /^(@?)(.*)/);
		if ($array) {
		    $name = $name."_aref";
		}
		push(@{$tables{$object}{creator}}, $name);
	    }
	}
	if ($scheme{$object}->{constructors}) {
	    foreach $constructor (@{$scheme{$object}->{constructors}}) {
		my @vars = ();
		foreach $var (@$constructor) {
		    my ($array, $name) = ($var =~ /^(@?)(.*)/);
		    if ($array) {
			$name = $name."_aref";
		    }
		    push(@vars, $name);
		}
		push(@{$tables{$object}{constructors}}, \@vars);
	    }
	}
    }

#    open(DUMP, "> $basename.dump") || die "can't open dump file\n";
#    print DUMP Dumper(\%tables);
#    close(DUMP);

    # create SQL statements to generate the tables and all necessary
    # helpers
    my $sql = mksql($basename);

    # create Perl code to interface the individual tables
    mkperl($basename, $backend);
}



#########################################################################
#
# take the scheme description from the hash, and create a relational
# description of the database
#
#########################################################################


sub mktable {
    my ($name, $memberref) = @_;
    my %members = %$memberref;

    # assume this is a second class table, if noone has voted against this
    if (!exists($tables{$name}{type})) {
	$tables{$name}{type} = '2';
    }
    # iterate over all members of the object, eventually normalizing
    foreach $member (keys(%members)) {
	# check for 1:n relation
	my ($many, $col) = ($member =~ /^(@?)(.*)/);
	# check type of member
	my $type = $members{$member};
	if ($many) {
	    # add primary key to table, as we are about to normalize
	    $tables{$name}{cols}{'id'} = 'pkey';
	    $tables{$name}{type} = '1';
	    $tables{$name.'_'.$col}{cols}{$name.'_id'} = 'fkey';
###
###
### add code to generate creator and constructors for normalized tables
###
###
	    mktable($name.'_'.$col, $type);
	} elsif (($reference) = ($type =~ /^ref on (.*)$/)) {
	    $tables{$name}{cols}{$col.'_id'} = "fkey $reference";
	    $tables{$reference}{cols}{'id'} = 'pkey';
	    $tables{$reference}{type} = '1';
	} else {
	    $tables{$name}{cols}{$member} = $type;
	}
    }
}



#########################################################################
#
# generate SQL statements from the relational description of the database
#
#########################################################################

sub mksql {
    my ($basename) = @_;
    my @counter = ();
    my $sql = '';

    # build the statements for each table
    foreach $table (keys(%tables)) {
	# if this is a first class table, create a counter
	if ($tables{$table}{type} eq '1') {
	    push(@counter, $table);
	}
	# the CREATE TABLE statement
	$sql .= "CREATE TABLE $table (\n";
	my @cols = ();
	foreach $col (keys(%{$tables{$table}{cols}})) {
	    my $type = $tables{$table}{cols}{$col};
	    if ($type eq 'pkey') {
		$type = 'int NOT NULL';
		push(@cols, "\tPRIMARY KEY ($col)");
	    }
	    if ($type =~ /^fkey/) {
		$type = 'int';
	    }
	    push(@cols, "\t$col $type");
	}
	$sql .= join(",\n", @cols) . "\n\t);\n";
	# if necessary, create some UNIQUE INDEX statements
	foreach $keys (@{$tables{$table}{constructors}}) {
	    my $keylist = join(', ', @$keys);
	    my $indexname = join('_', $table, @$keys).'_key';
	    $sql .= "CREATE UNIQUE INDEX $indexname ON $table ($keylist);\n";
	}
    }

    # create a table with all counters
    $sql .= <<SQL_END;
CREATE TABLE $basename\_counters (
	object char(30),
	val int);
SQL_END
    foreach $table (@counter) {
	$sql .= "INSERT INTO $basename\_counters (object, val) VALUES ('$table', 0);\n";
    }

    # write the SQL description to a file
    open(SQL, "> $basename\.sql") || die "can't open SQL file\n";
    print SQL $sql;
    close(SQL);
}



#########################################################################
#
# create Perl modules to interface the database
#
#########################################################################

sub mkperl {
    my ($basename, $backend) = @_;
    
    # create a directory that contains all modules
    if (!-d $basename) {
	mkdir($basename, 0755);
    }

    # create a module to contact the database
    mkdbimodule($basename, $backend);

    # create one module for each first class table
    foreach $table (keys(%tables)) {
	if ($tables{$table}{type} eq '1') {
	    mkobjmodule($basename, $table);
	}
    }
}


# create a module to contact the database. this module exports a database
# handle and is 'use'd by all other modules
sub mkdbimodule {
    my ($basename, $backend) = @_;
    my $lcname = lc($basename);

    my $perl = <<PERL_END;
package $basename\::DBMS;

use DBI;

require Exporter;
\@ISA = qw{Exporter};
\@EXPORT = qw{\$$basename\_DBH newid};

PERL_END
    if ($backend eq 'postgres') {
	$perl .=
	    "\$$basename\_DBH = DBI->connect('dbi:Pg:dbname=$lcname', '', '')\n";
    } elsif ($backend eq 'mysql') {
	$perl .= <<PERL_END
my \$mysqlhost = \$ENV{'MYSQL_HOST'};
\$$basename\_DBH = DBI->connect("DBI:mysql:$lcname:\$mysqlhost", '', '')
PERL_END
    }
    $perl .= <<PERL_END;
    || die "can't connect to database: \$!\\n";

sub newid {
    my (\$table) = \@_;
PERL_END
    if ($backend eq 'postgres') {
	$perl .= <<PERL_END;
    \$$basename\_DBH->{AutoCommit} = 0;
    \$$basename\_DBH->do(qq {
		LOCK $basename\_counters
	}) || return(-1);
PERL_END
    } elsif ($backend eq 'mysql') {
	$perl .= <<PERL_END;
    \$$basename\_DBH->do(qq {
		LOCK TABLES $basename\_counters WRITE
	}) || return(-1);
PERL_END
    }
    $perl .= <<PERL_END;
    my \$sth = \$$basename\_DBH->prepare(qq {
		SELECT val FROM $basename\_counters WHERE object='\$table'
	});
    \$sth->execute;
    my (\$curval) = \$sth->fetchrow_array;
    \$sth->finish;
    \$curval++;
    \$$basename\_DBH->do(qq {
	UPDATE $basename\_counters SET val=\$curval WHERE object='\$table'
	});
PERL_END
    if ($backend eq 'postgres') {
	$perl .= <<PERL_END;
    \$$basename\_DBH->commit;
    \$$basename\_DBH->{AutoCommit} = 1;
PERL_END
    } elsif ($backend eq 'mysql') {
	$perl .= <<PERL_END;
    \$$basename\_DBH->do(qq {
		UNLOCK TABLES
    }) || return(-1);
PERL_END
    }
    $perl .= <<PERL_END;
    return(\$curval);
}
PERL_END

    open(FILE, "> $basename/DBMS.pm") || die "can't open DBMS.pm\n";
    print FILE $perl;
    close(FILE);
}


# create one module to interface a first class table. this module includes
# constructors for new and existing entries in the database, and methods to
# access and modify the member variables
sub mkobjmodule {
    my ($basename, $table) = @_;

    my $perl = <<PERL_END;
########################################################################
#
# This module was created automagically by O2DBI ($VERSION)
# Do not modify this file, changes will be lost!!!
#
# Additional methods can be defined in the file $basename\::$table\_add.pm.
#
########################################################################

package $basename\::$table;

use $basename\::DBMS;

1;

########################################################################
#
# constructor and destructor methods for $table
#
########################################################################

PERL_END

    # add a create method
    $perl .= mkcreator($basename, $table, $tables{$table}{creator});
    # add methods for each constructor to
    #  - initialize one object
    #  - all objects in a hash
    foreach $constructor ([ 'id' ], @{$tables{$table}{constructors}}) {
	$perl .= mkconstructor($basename, $table, $constructor);
	$perl .= mkfetchallhash($basename, $table, $constructor);
    }
    $perl .= mkfetchbySQL($basename, $table);
    # add method to fetch all objects in an array
    $perl .= mkfetchallarray($basename, $table);
    # add a delete method
    $perl .= mkdelete($basename, $table);
    $perl .= <<PERL_END;
########################################################################
#
# methods to access the member variables
#
########################################################################

PERL_END
    # add methods to get or set the member variables
    foreach $col (keys(%{$tables{$table}{cols}})) {
	$perl .= mkmemberaccess($basename, $table, $col);
    }
    # add a method to set multiple members at the same time
    $perl .= mkmset($basename, $table);
    $perl .= <<PERL_END;
########################################################################
#
# load additional methods from self made module
#
########################################################################

require $basename\::$table\_add;

########################################################################
#
# private functions used inside this module
#
########################################################################

PERL_END
    # add some generic functions, e.g. the getset method
    $perl .= mkmisc($basename, $table);

    # write the code to a file
    open(FILE, "> $basename/$table\.pm") || die "can't open module file\n";
    print FILE $perl;
    close(FILE);

    # if it doesn't exist, create a template module for additional methods
    if (-f "$basename/$table\_add.pm") {
	print "not regenerating $basename/$table\_add.pm\n";
    } else {
	$perl = mkadd($basename, $table);
	open(FILE, "> $basename/$table\_add.pm")
	    || die "can't open module file\n";
	print FILE $perl;
        close(FILE);
    }
}


# write a method to create a new entry.
sub mkcreator {
    my ($basename, $table, $colref) = @_;
    my @cols = @$colref;
###
###
### insert code to fetch foreign keys and insert them into the 1:n tables
###
###	    
    my $cols = join(', ', @cols);
    my $vars = join(', ', map("\$".$_, @cols));
    my $qvars = join(', ', map("'\$".$_."'", @cols));
    my $perl = <<PERL_END;
# create a new object and insert it into the database
sub create {
    my (\$class, $vars) = \@_;
    # fetch a fresh id
    my \$id = newid('$table');
        if (\$id < 0) {
	return(-1);
    }
    # insert the primary key into the database
    \$$basename\_DBH->do(qq {
            INSERT INTO $table (id) VALUES (\$id)
           });
    if (\$$basename\_DBH->err) {
	return(-1);
    }
    # create the perl object
    my \$$table = { 'id' => \$id,
		    '_buffer' => 1 };
    bless(\$$table, \$class);
    # fill in the remaining data
PERL_END
    foreach $var (@cols) {
	$perl .= "    \$$table->$var(\$$var);\n";
    }
    $perl .= <<PERL_END;
    if (\$$table->unbuffer < 0) {
	\$$table->delete;
	return(-1);
    } else {
	return(\$$table);
    }
}

PERL_END
    return($perl);
}


# write a method to initialize a new object based on existing data
sub mkconstructor {
    my ($basename, $table, $keysref) = @_;
    my @keys = @$keysref;
    my $params = join(', ', map("\$req_".$_, @keys));
    my $sqlrestrict = join(' AND ', map("$_='\$req_$_'", @keys));
    my @cols = (keys(%{$tables{$table}{cols}}));
    my $cols = join(', ', @cols);
    my $vars = join(', ', map("\$".$_, @cols));
    my $qvars = join(', ', map("'\$".$_."'", @cols));
    my $method = "init_".join('_', @keys);
    my $perl = <<PERL_END;
# create an object for already existing data
sub $method {
    my (\$class, $params) = \@_;
    # fetch the data from the database
    my \$sth = \$$basename\_DBH->prepare(qq {
	SELECT $cols FROM $table
		WHERE $sqlrestrict
	});
    \$sth->execute;
    my ($vars) = \$sth->fetchrow_array;
    \$sth->finish;
    # if successful, return an appropriate object
    if (!defined(\$id)) {
	return(-1);
    } else {
	my \$$table = {
PERL_END
    my @hashdesc = ();
    foreach $var (@cols) {
	push(@hashdesc, "'$var' => \$$var");
    }
    $perl .= "\t\t".join(", \n\t\t", @hashdesc)."\n\t\t};\n";
    $perl .= <<PERL_END;
        bless(\$$table, \$class);
        return(\$$table);
    }
}

PERL_END
    
    return($perl);
}


# write method to create a hash of all objects, index by one of the
# constructor keys
sub mkfetchallhash {
    my ($basename, $table, $keysref) = @_;
    my @keys = @$keysref;
    my $key = join(', ', map("\$".$_, @keys));
    my @cols = (keys(%{$tables{$table}{cols}}));
    my $cols = join(', ', @cols);
    my $vars = join(', ', map("\$".$_, @cols));
    my $qvars = join(', ', map("'\$".$_."'", @cols));
    my $method = "fetchallby_".join('_', @keys);
    my $perl = <<PERL_END;
# get all objects from the database efficiently and return a hash reference
sub $method {
    my (\$class) = \@_;
    local \%$table = ();
    my \$sth = \$$basename\_DBH->prepare(qq {
	SELECT $cols FROM $table
	});
    \$sth->execute;
    while (($vars) = \$sth->fetchrow_array) {
	my \$$table = {
PERL_END
    my @hashdesc = ();
    foreach $var (@cols) {
	push(@hashdesc, "'$var' => \$$var");
    }
    $perl .= "\t\t".join(", \n\t\t", @hashdesc)."\n\t\t};\n";
    $perl .= <<PERL_END;
	bless(\$$table, \$class);
PERL_END
    if ($#keys > 0) {
	$perl .= <<PERL_END;
	my \$key = join(',', $key);
	\$$table\{\$key} = \$$table;
PERL_END
    } else {
	$perl .= <<PERL_END;
	\$$table\{$key} = \$$table;
PERL_END
    }
    $perl .= <<PERL_END;
    }
    \$sth->finish;
    return(\\%$table);
}

PERL_END
    return($perl);
}


# write method to create an array of all objects
sub mkfetchallarray {
    my ($basename, $table) = @_;
    my @cols = (keys(%{$tables{$table}{cols}}));
    my $cols = join(', ', @cols);
    my $vars = join(', ', map("\$".$_, @cols));
    my $qvars = join(', ', map("'\$".$_."'", @cols));
    my $perl .= <<PERL_END;
# get all objects from the database efficiently and return an array reference
sub fetchall {
    my (\$class) = \@_;
    local \@$table = ();
    my \$sth = \$$basename\_DBH->prepare(qq {
	SELECT $cols FROM $table
	});
    \$sth->execute;
    while (($vars) = \$sth->fetchrow_array) {
	my \$$table = {
PERL_END
    my @hashdesc = ();
    foreach $var (@cols) {
	push(@hashdesc, "'$var' => \$$var");
    }
    $perl .= "\t\t".join(", \n\t\t", @hashdesc)."\n\t\t};\n";
    $perl .= <<PERL_END;
	bless(\$$table, \$class);
	push(\@$table, \$$table);
    }
    \$sth->finish;
    return(\\\@$table);
}

PERL_END
    return($perl);
}


# write method to create an array of selected objects, depending on
# a given SQL WHERE clause
sub mkfetchbySQL {
    my ($basename, $table) = @_;
    my @cols = (keys(%{$tables{$table}{cols}}));
    my $cols = join(', ', @cols);
    my $vars = join(', ', map("\$".$_, @cols));
    my $qvars = join(', ', map("'\$".$_."'", @cols));
    my $perl .= <<PERL_END;
# get all those objects from the database efficiently that conform to the
# given WHERE clause and return an array reference
sub fetchbySQL {
    my (\$class, \$statement) = \@_;
    local \@$table = ();
    my \$sth = \$$basename\_DBH->prepare(qq {
	SELECT $cols FROM $table WHERE \$statement
	});
    \$sth->execute;
    while (($vars) = \$sth->fetchrow_array) {
	my \$$table = {
PERL_END
    my @hashdesc = ();
    foreach $var (@cols) {
	push(@hashdesc, "'$var' => \$$var");
    }
    $perl .= "\t\t".join(", \n\t\t", @hashdesc)."\n\t\t};\n";
    $perl .= <<PERL_END;
	bless(\$$table, \$class);
	push(\@$table, \$$table);
    }
    \$sth->finish;
    return(\\\@$table);
}

PERL_END
    return($perl);
}


# write a method to delete an object completely from the database
sub mkdelete {
    my ($basename, $table) = @_;
    my $perl = <<PERL_END;
# delete an object completely from the database
sub delete {
    my (\$self) = \@_;
    my \$id = \$self->id;
    \$$basename\_DBH->do(qq {
	DELETE FROM $table WHERE id=\$id
	}) || return(-1);
    undef(\$self);
}

PERL_END
    return($perl);
}


# write method to access the member variables
sub mkmemberaccess {
    my ($basename, $table, $var) = @_;
    my $perl = '';
    # the object id is read only
    if ($var eq 'id') {
	$perl .= <<PERL_END;
# get the member variable '$var'
sub $var {
    my (\$self) = \@_;
    return(\$self->{'id'});
}

PERL_END
    } else {
        # if the member references an object, use it
        if (($class) = ($tables{$table}{cols}{$var} =~ /^fkey (.*)$/)) {
	    my ($member) = ($var =~ (/(.*)_id$/));
	    $perl .= <<PERL_END;
# get or set the object '$member'
sub $member {
    my (\$self, \$$member) = \@_;
    if (defined(\$$member)) {
	return(\$self->getset('$var', \$$member->id));
    } else {
	my \$id = \$self->{'$var'};
	return($basename\::$class->init_id(\$id));
    }
}

PERL_END
         } else {
             $perl .= <<PERL_END
# get or set the member variable '$var'
sub $var {
    my (\$self, \$$var) = \@_;
    return(\$self->getset('$var', \$$var));
}

PERL_END
         }
    }
    return($perl);
}


# write a method to set multiple variables at the same time. this breaks
# the OO view a little bit, but is much more efficient than have 20
# consecutive calls of member functions
sub mkmset {
    my ($basename, $table) = @_;
    my $perl = <<PERL_END;
# set several member variables at the same time
sub mset {
    my (\$self, \$hashref) = \@_;
    my \$curbuffer = \$self->buffered;
    \$self->buffer;
    foreach \$key (keys(\%\$hashref)) {
	# prevent really stupid tricks
	if (\$key eq 'id') {
	    return(-1);
	}
	my \$val = \$hashref->{\$key};
	\&\$key(\$self, \$val);
    }
    if (!\$curbuffer) {
	\$self->unbuffer;
    }
}

PERL_END
    return($perl);
}


# write helper functions used by the module
sub mkmisc {
    my ($basename, $table) = @_;
    my $perl = <<PERL_END;
# test if the data is buffered or passed to the DBMS immediately
sub buffered {
    my (\$self) = \@_;
    return(\$self->{'_buffer'});
}

# make the data buffered, i.e. don't write to the database
sub buffer {
    my (\$self) = \@_;
    \$self->{'_buffer'} = 1;
}

# write the current contents to the database and declare the object unbuffered
sub unbuffer {
    my (\$self) = \@_;
    if (\$self->buffered) {
	my \@sql = ();
PERL_END
    my $cols = join(' ', keys(%{$tables{$table}{cols}}));
    $perl .= <<PERL_END;
	foreach \$key (qw{$cols}) {
	    push(\@sql, "\$key=".\$$basename\_DBH->quote(\$self->{\$key}));
	}
	my \$id = \$self->id;
	my \$sql = "UPDATE $table SET ".join(', ', \@sql)." WHERE id=\$id";
	\$$basename\_DBH->do(\$sql) || return(-1);
    }
    \$self->{'_buffer'} = 0;
}

# get or set one of the member variables
sub getset {
    my (\$self, \$var, \$val) = \@_;
    my \$id = \$self->id;
    if (defined(\$val)) {
	if (!\$self->buffered) {
	    my \$qval = \$$basename\_DBH->quote(\$val);
	    \$$basename\_DBH->do(qq {
		UPDATE $table SET \$var=\$qval WHERE id=\$id
		}) || return(-1);
	}
	\$self->{\$var} = \$val;
    }
    return(\$self->{\$var});
}

PERL_END
    return($perl);
}


# generate additional module for private methods
sub mkadd {
    my ($basename, $table) = @_;
    $perl = <<PERL_END;
########################################################################
#
# This module defines extensions to the automagically created file
# $table.pm. Add your own code below.
#
########################################################################

1;

# sub foo {
#     my (\$self, \$arg1, \$arg2) = \@_;
#     ....
#     return(\$result);
# }
PERL_END
    return($perl);
}
