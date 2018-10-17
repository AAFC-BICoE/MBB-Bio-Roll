#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Date-Manip
#    Version:           6.72
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Date\:\:Manip
#

Name:           opt-perl-Date-Manip
Version:        6.72
Release:        1%{?dist}
Summary:        Date manipulation routines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Date-Manip/
BuildRoot:      /tmp/cpantorpm/Date-Manip-6.72-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SB/SBECK/Date-Manip-6.72.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Date::Manip) = 6.72
Provides:       opt-perl(Date::Manip::Base) = 6.72
Provides:       opt-perl(Date::Manip::DM5) = 6.72
Provides:       opt-perl(Date::Manip::DM5abbrevs) = 6.72
Provides:       opt-perl(Date::Manip::DM6) = 6.72
Provides:       opt-perl(Date::Manip::Date) = 6.72
Provides:       opt-perl(Date::Manip::Delta) = 6.72
Provides:       opt-perl(Date::Manip::Lang::catalan) = 6.72
Provides:       opt-perl(Date::Manip::Lang::danish) = 6.72
Provides:       opt-perl(Date::Manip::Lang::dutch) = 6.72
Provides:       opt-perl(Date::Manip::Lang::english) = 6.72
Provides:       opt-perl(Date::Manip::Lang::finnish) = 6.72
Provides:       opt-perl(Date::Manip::Lang::french) = 6.72
Provides:       opt-perl(Date::Manip::Lang::german) = 6.72
Provides:       opt-perl(Date::Manip::Lang::index) = 6.72
Provides:       opt-perl(Date::Manip::Lang::italian) = 6.72
Provides:       opt-perl(Date::Manip::Lang::norwegian) = 6.72
Provides:       opt-perl(Date::Manip::Lang::polish) = 6.72
Provides:       opt-perl(Date::Manip::Lang::portugue) = 6.72
Provides:       opt-perl(Date::Manip::Lang::romanian) = 6.72
Provides:       opt-perl(Date::Manip::Lang::russian) = 6.72
Provides:       opt-perl(Date::Manip::Lang::spanish) = 6.72
Provides:       opt-perl(Date::Manip::Lang::swedish) = 6.72
Provides:       opt-perl(Date::Manip::Lang::turkish) = 6.72
Provides:       opt-perl(Date::Manip::Obj) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off000) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off001) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off002) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off003) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off004) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off005) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off006) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off007) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off008) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off009) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off010) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off011) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off012) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off013) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off014) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off015) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off016) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off017) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off018) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off019) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off020) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off021) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off022) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off023) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off024) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off025) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off026) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off027) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off028) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off029) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off030) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off031) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off032) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off033) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off034) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off035) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off036) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off037) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off038) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off039) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off040) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off041) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off042) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off043) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off044) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off045) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off046) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off047) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off048) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off049) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off050) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off051) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off052) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off053) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off054) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off055) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off056) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off057) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off058) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off059) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off060) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off061) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off062) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off063) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off064) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off065) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off066) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off067) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off068) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off069) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off070) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off071) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off072) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off073) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off074) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off075) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off076) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off077) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off078) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off079) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off080) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off081) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off082) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off083) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off084) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off085) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off086) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off087) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off088) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off089) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off090) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off091) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off092) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off093) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off094) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off095) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off096) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off097) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off098) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off099) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off100) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off101) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off102) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off103) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off104) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off105) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off106) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off107) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off108) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off109) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off110) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off111) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off112) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off113) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off114) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off115) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off116) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off117) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off118) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off119) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off120) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off121) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off122) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off123) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off124) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off125) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off126) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off127) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off128) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off129) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off130) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off131) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off132) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off133) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off134) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off135) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off136) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off137) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off138) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off139) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off140) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off141) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off142) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off143) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off144) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off145) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off146) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off147) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off148) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off149) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off150) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off151) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off152) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off153) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off154) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off155) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off156) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off157) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off158) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off159) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off160) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off161) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off162) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off163) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off164) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off165) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off166) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off167) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off168) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off169) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off170) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off171) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off172) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off173) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off174) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off175) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off176) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off177) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off178) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off179) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off180) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off181) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off182) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off183) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off184) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off185) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off186) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off187) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off188) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off189) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off190) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off191) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off192) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off193) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off194) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off195) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off196) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off197) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off198) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off199) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off200) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off201) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off202) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off203) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off204) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off205) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off206) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off207) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off208) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off209) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off210) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off211) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off212) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off213) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off214) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off215) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off216) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off217) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off218) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off219) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off220) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off221) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off222) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off223) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off224) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off225) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off226) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off227) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off228) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off229) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off230) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off231) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off232) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off233) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off234) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off235) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off236) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off237) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off238) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off239) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off240) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off241) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off242) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off243) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off244) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off245) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off246) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off247) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off248) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off249) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off250) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off251) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off252) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off253) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off254) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off255) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off256) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off257) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off258) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off259) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off260) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off261) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off262) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off263) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off264) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off265) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off266) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off267) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off268) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off269) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off270) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off271) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off272) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off273) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off274) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off275) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off276) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off277) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off278) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off279) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off280) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off281) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off282) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off283) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off284) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off285) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off286) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off287) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off288) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off289) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off290) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off291) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off292) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off293) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off294) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off295) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off296) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off297) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off298) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off299) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off300) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off301) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off302) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off303) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off304) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off305) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off306) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off307) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off308) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off309) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off310) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off311) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off312) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off313) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off314) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off315) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off316) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off317) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off318) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off319) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off320) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off321) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off322) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off323) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off324) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off325) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off326) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off327) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off328) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off329) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off330) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off331) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off332) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off333) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off334) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off335) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off336) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off337) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off338) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off339) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off340) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off341) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off342) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off343) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off344) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off345) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off346) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off347) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off348) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off349) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off350) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off351) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off352) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off353) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off354) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off355) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off356) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off357) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off358) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off359) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off360) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off361) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off362) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off363) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off364) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off365) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off366) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off367) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off368) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off369) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off370) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off371) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off372) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off373) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off374) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off375) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off376) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off377) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off378) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off379) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off380) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off381) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off382) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off383) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off384) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off385) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off386) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off387) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off388) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off389) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off390) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off391) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off392) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off393) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off394) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off395) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off396) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off397) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off398) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off399) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off400) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off401) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off402) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off403) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off404) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off405) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off406) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off407) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off408) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off409) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off410) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off411) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off412) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off413) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off414) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off415) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off416) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off417) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off418) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off419) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off420) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off421) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off422) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off423) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off424) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off425) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off426) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off427) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off428) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off429) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off430) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off431) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off432) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off433) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off434) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off435) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off436) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off437) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off438) = 6.72
Provides:       opt-perl(Date::Manip::Offset::off439) = 6.72
Provides:       opt-perl(Date::Manip::Recur) = 6.72
Provides:       opt-perl(Date::Manip::TZ) = 6.72
Provides:       opt-perl(Date::Manip::TZ::a00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afabid00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afaccr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afalgi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afbiss00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afcair00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afcasa00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afceut00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afel_a00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afjoha00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afjuba00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afkhar00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aflago00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afmapu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afmonr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afnair00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afndja00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afsao_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aftrip00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aftuni00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::afwind00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amadak00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amanch00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amarag00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amasun00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amatik00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambahi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambahi01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambarb00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambele00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambeli00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambeul00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amblan00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amboa_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambogo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambois00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ambuen00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcamb00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcamp00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcanc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcara00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcata00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcaye00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcent00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amchic00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amchih00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcord00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcost00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcres00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcuia00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amcura00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amdanm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amdaws00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amdaws01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amdenv00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amdetr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amedmo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ameiru00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amel_s00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amfort00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amfort01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amglac00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amgodt00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amgoos00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amgran00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amguat00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amguay00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amguya00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amhali00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amhava00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amherm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amindi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aminuv00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amiqal00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amjama00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amjuju00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amjune00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amknox00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amla_p00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amla_r00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amlima00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amlos_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amloui00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammace00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammana00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammana01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammare00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammart00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammata00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammaza00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammend00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammeno00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammeri00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammetl00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammexi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammiqu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammonc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammont00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammont01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ammont02) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnass00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnew_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnew_01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnipi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnome00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amnoro00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amojin00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampana00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampang00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampara00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampete00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amphoe00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amport00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amport01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amport02) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampuer00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ampunt00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amrain00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amrank00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amreci00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amregi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amreso00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amrio_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amrio_01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsalt00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsan_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsan_01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsant00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsant01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsant02) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsao_00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amscor00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amsitk00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amst_j00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amswif00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amtegu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amtell00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amthul00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amthun00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amtiju00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amtoro00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amtucu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amushu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amvanc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amveva00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amvinc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amwhit00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amwina00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amwinn00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amyaku00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::amyell00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ancase00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::andavi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::andumo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::anmacq00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::anmaws00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::anpalm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::anroth00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ansyow00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::antrol00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::anvost00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asalma00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asamma00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asanad00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asaqta00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asaqto00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asashg00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asatyr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbagh00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbaku00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbang00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbarn00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbeir00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbish00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asbrun00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aschit00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aschoi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ascolo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asdama00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asdhak00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asdili00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asduba00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asdush00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asfama00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asgaza00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ashebr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asho_c00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ashong00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ashovd00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asirku00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asjaka00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asjaya00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asjeru00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askabu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askamc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askara00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askath00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askhan00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askolk00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askras00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askual00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::askuch00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asmaca00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asmaga00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asmaka00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asmani00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asnico00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asnovo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asnovo01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asomsk00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asoral00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aspont00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aspyon00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asqata00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asqyzy00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asriya00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::assakh00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::assama00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asseou00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asshan00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::assing00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::assred00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astaip00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astash00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astbil00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astehr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asthim00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astoky00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::astoms00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asulaa00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asurum00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asustm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asvlad00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asyaku00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asyang00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asyeka00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::asyere00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atazor00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atberm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atcana00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atcape00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atfaro00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atmade00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atreyk00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atsout00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::atstan00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::auadel00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aubris00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aubrok00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aucurr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::audarw00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aueucl00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::auhoba00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aulind00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aulord00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aumelb00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::aupert00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ausydn00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::b00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::c00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::cet00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::d00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::e00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eet00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmt00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm02) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm03) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm04) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm05) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm06) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm07) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm08) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm09) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm10) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm11) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm12) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtm13) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp01) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp02) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp03) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp04) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp05) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp06) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp07) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp08) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp09) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp10) = 6.72
Provides:       opt-perl(Date::Manip::TZ::etgmtp11) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euamst00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euando00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euastr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euathe00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eubelg00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euberl00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eubrus00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eubuch00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eubuda00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euchis00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eucope00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eudubl00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eugibr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euhels00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euista00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eukali00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eukiev00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eukiro00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eulisb00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eulond00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euluxe00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eumadr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eumalt00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eumins00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eumona00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eumosc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euoslo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eupari00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euprag00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euriga00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eurome00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eusama00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eusara00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eusimf00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eusofi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eustoc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eutall00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::eutira00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euulya00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euuzhg00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euvien00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euviln00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euvolg00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euwars00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euzapo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::euzuri00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::f00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::g00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::h00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::i00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inchag00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inchri00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::incoco00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inkerg00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inmahe00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inmald00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inmaur00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::inreun00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::k00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::l00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::m00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::met00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::n00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::o00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::p00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paapia00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paauck00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paboug00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pachat00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pachuu00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paeast00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paefat00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paende00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pafaka00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pafiji00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pafuna00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pagala00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pagamb00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paguad00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paguam00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pahono00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pakiri00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pakosr00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pakwaj00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pamaju00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pamarq00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::panaur00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paniue00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::panorf00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::panoum00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::papago00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::papala00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::papitc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::papohn00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::paport00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pararo00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::patahi00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::patara00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::patong00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pawake00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::pawall00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::q00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::r00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::s00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::t00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::u00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::ut00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::utc00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::v00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::w00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::wet00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::x00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::y00) = 6.72
Provides:       opt-perl(Date::Manip::TZ::z00) = 6.72
Provides:       opt-perl(Date::Manip::TZ_Base) = 6.72
Provides:       opt-perl(Date::Manip::TZdata) = 6.72
Provides:       opt-perl(Date::Manip::Zones) = 6.72
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Cwd)
Requires:       opt-perl(Data::Dumper)
Requires:       opt-perl(Encode)
Requires:       opt-perl(File::Find)
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(IO::File)
Requires:       opt-perl(Storable)
Requires:       opt-perl(utf8)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Cwd)
BuildRequires:  opt-perl(Data::Dumper)
BuildRequires:  opt-perl(Encode)
BuildRequires:  opt-perl(File::Find)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(IO::File)
BuildRequires:  opt-perl(Storable)
BuildRequires:  opt-perl(utf8)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Date-Manip-6.72
chmod -R u+w %{_builddir}/Date-Manip-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/bin/*
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 6.72-1
- Generated using cpantorpm

