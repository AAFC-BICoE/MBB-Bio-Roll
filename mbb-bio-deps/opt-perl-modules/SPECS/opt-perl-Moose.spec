#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Moose
#    Version:           2.2011
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Moose
#

Name:           opt-perl-Moose
Version:        2.2011
Release:        1%{?dist}
Summary:        A postmodern object system for Perl 5
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Moose/
BuildRoot:      /tmp/cpantorpm/Moose-2.2011-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/E/ET/ETHER/Moose-2.2011.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Class::MOP) = 2.2011
Provides:       opt-perl(Class::MOP::Attribute) = 2.2011
Provides:       opt-perl(Class::MOP::Class) = 2.2011
Provides:       opt-perl(Class::MOP::Instance) = 2.2011
Provides:       opt-perl(Class::MOP::Method) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Accessor) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Constructor) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Generated) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Inlined) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Meta) = 2.2011
Provides:       opt-perl(Class::MOP::Method::Wrapped) = 2.2011
Provides:       opt-perl(Class::MOP::Module) = 2.2011
Provides:       opt-perl(Class::MOP::Object) = 2.2011
Provides:       opt-perl(Class::MOP::Overload) = 2.2011
Provides:       opt-perl(Class::MOP::Package) = 2.2011
Provides:       opt-perl(Moose) = 2.2011
Provides:       opt-perl(Moose::Cookbook) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::BankAccount_MethodModifiersAndSubclassing) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::BinaryTree_AttributeFeatures) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::BinaryTree_BuilderAndLazyBuild) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Company_Subtypes) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::DateTime_ExtendingNonMooseParent) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Document_AugmentAndInner) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Genome_OverloadingSubtypesAndCoercion) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::HTTP_SubtypesAndCoercion) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Immutable) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Person_BUILDARGSAndBUILD) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Basics::Point_AttributesAndSubclassing) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Extending::Debugging_BaseClassRole) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Extending::ExtensionOverview) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Extending::Mooseish_MooseSugar) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Legacy::Debugging_BaseClassReplacement) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Legacy::Labeled_AttributeMetaclass) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Legacy::Table_ClassMetaclass) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Meta::GlobRef_InstanceMetaclass) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Meta::Labeled_AttributeTrait) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Meta::PrivateOrPublic_MethodMetaclass) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Meta::Table_MetaclassTrait) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Meta::WhyMeta) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Roles::ApplicationToInstance) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Roles::Comparable_CodeReuse) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Roles::Restartable_AdvancedComposition) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Snack::Keywords) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Snack::Types) = 2.2011
Provides:       opt-perl(Moose::Cookbook::Style) = 2.2011
Provides:       opt-perl(Moose::Exception) = 2.2011
Provides:       opt-perl(Moose::Exception::AccessorMustReadWrite) = 2.2011
Provides:       opt-perl(Moose::Exception::AddParameterizableTypeTakesParameterizableType) = 2.2011
Provides:       opt-perl(Moose::Exception::AddRoleTakesAMooseMetaRoleInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::AddRoleToARoleTakesAMooseMetaRole) = 2.2011
Provides:       opt-perl(Moose::Exception::ApplyTakesABlessedInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::AttachToClassNeedsAClassMOPClassInstanceOrASubclass) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeConflictInRoles) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeConflictInSummation) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeExtensionIsNotSupportedInRoles) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeIsRequired) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeMustBeAnClassMOPMixinAttributeCoreOrSubclass) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeNamesDoNotMatch) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeValueIsNotAnObject) = 2.2011
Provides:       opt-perl(Moose::Exception::AttributeValueIsNotDefined) = 2.2011
Provides:       opt-perl(Moose::Exception::AutoDeRefNeedsArrayRefOrHashRef) = 2.2011
Provides:       opt-perl(Moose::Exception::BadOptionFormat) = 2.2011
Provides:       opt-perl(Moose::Exception::BothBuilderAndDefaultAreNotAllowed) = 2.2011
Provides:       opt-perl(Moose::Exception::BuilderDoesNotExist) = 2.2011
Provides:       opt-perl(Moose::Exception::BuilderMethodNotSupportedForAttribute) = 2.2011
Provides:       opt-perl(Moose::Exception::BuilderMethodNotSupportedForInlineAttribute) = 2.2011
Provides:       opt-perl(Moose::Exception::BuilderMustBeAMethodName) = 2.2011
Provides:       opt-perl(Moose::Exception::CallingMethodOnAnImmutableInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::CallingReadOnlyMethodOnAnImmutableInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::CanExtendOnlyClasses) = 2.2011
Provides:       opt-perl(Moose::Exception::CanOnlyConsumeRole) = 2.2011
Provides:       opt-perl(Moose::Exception::CanOnlyWrapBlessedCode) = 2.2011
Provides:       opt-perl(Moose::Exception::CanReblessOnlyIntoASubclass) = 2.2011
Provides:       opt-perl(Moose::Exception::CanReblessOnlyIntoASuperclass) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAddAdditionalTypeCoercionsToUnion) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAddAsAnAttributeToARole) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotApplyBaseClassRolesToRole) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAssignValueToReadOnlyAccessor) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAugmentIfLocalMethodPresent) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAugmentNoSuperMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAutoDerefWithoutIsa) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotAutoDereferenceTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCalculateNativeType) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCallAnAbstractBaseMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCallAnAbstractMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCoerceAWeakRef) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCoerceAttributeWhichHasNoCoercion) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCreateHigherOrderTypeWithoutATypeParameter) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCreateMethodAliasLocalMethodIsPresent) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotCreateMethodAliasLocalMethodIsPresentInClass) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotDelegateLocalMethodIsPresent) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotDelegateWithoutIsa) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotFindDelegateMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotFindType) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotFindTypeGivenToMatchOnType) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotFixMetaclassCompatibility) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotGenerateInlineConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotInitializeMooseMetaRoleComposite) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotInlineTypeConstraintCheck) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotLocatePackageInINC) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotMakeMetaclassCompatible) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotOverrideALocalMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotOverrideBodyOfMetaMethods) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotOverrideLocalMethodIsPresent) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotOverrideNoSuperMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotRegisterUnnamedTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::CannotUseLazyBuildAndDefaultSimultaneously) = 2.2011
Provides:       opt-perl(Moose::Exception::CircularReferenceInAlso) = 2.2011
Provides:       opt-perl(Moose::Exception::ClassDoesNotHaveInitMeta) = 2.2011
Provides:       opt-perl(Moose::Exception::ClassDoesTheExcludedRole) = 2.2011
Provides:       opt-perl(Moose::Exception::ClassNamesDoNotMatch) = 2.2011
Provides:       opt-perl(Moose::Exception::CloneObjectExpectsAnInstanceOfMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::CodeBlockMustBeACodeRef) = 2.2011
Provides:       opt-perl(Moose::Exception::CoercingWithoutCoercions) = 2.2011
Provides:       opt-perl(Moose::Exception::CoercionAlreadyExists) = 2.2011
Provides:       opt-perl(Moose::Exception::CoercionNeedsTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::ConflictDetectedInCheckRoleExclusions) = 2.2011
Provides:       opt-perl(Moose::Exception::ConflictDetectedInCheckRoleExclusionsInToClass) = 2.2011
Provides:       opt-perl(Moose::Exception::ConstructClassInstanceTakesPackageName) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotCreateMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotCreateWriter) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotEvalConstructor) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotEvalDestructor) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotFindTypeConstraintToCoerceFrom) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotGenerateInlineAttributeMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotLocateTypeConstraintForUnion) = 2.2011
Provides:       opt-perl(Moose::Exception::CouldNotParseType) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateMOPClassTakesArrayRefOfAttributes) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateMOPClassTakesArrayRefOfSuperclasses) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateMOPClassTakesHashRefOfMethods) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateTakesArrayRefOfRoles) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateTakesHashRefOfAttributes) = 2.2011
Provides:       opt-perl(Moose::Exception::CreateTakesHashRefOfMethods) = 2.2011
Provides:       opt-perl(Moose::Exception::DefaultToMatchOnTypeMustBeCodeRef) = 2.2011
Provides:       opt-perl(Moose::Exception::DelegationToAClassWhichIsNotLoaded) = 2.2011
Provides:       opt-perl(Moose::Exception::DelegationToARoleWhichIsNotLoaded) = 2.2011
Provides:       opt-perl(Moose::Exception::DelegationToATypeWhichIsNotAClass) = 2.2011
Provides:       opt-perl(Moose::Exception::DoesRequiresRoleName) = 2.2011
Provides:       opt-perl(Moose::Exception::EnumCalledWithAnArrayRefAndAdditionalArgs) = 2.2011
Provides:       opt-perl(Moose::Exception::EnumValuesMustBeString) = 2.2011
Provides:       opt-perl(Moose::Exception::ExtendsMissingArgs) = 2.2011
Provides:       opt-perl(Moose::Exception::HandlesMustBeAHashRef) = 2.2011
Provides:       opt-perl(Moose::Exception::IllegalInheritedOptions) = 2.2011
Provides:       opt-perl(Moose::Exception::IllegalMethodTypeToAddMethodModifier) = 2.2011
Provides:       opt-perl(Moose::Exception::IncompatibleMetaclassOfSuperclass) = 2.2011
Provides:       opt-perl(Moose::Exception::InitMetaRequiresClass) = 2.2011
Provides:       opt-perl(Moose::Exception::InitializeTakesUnBlessedPackageName) = 2.2011
Provides:       opt-perl(Moose::Exception::InstanceBlessedIntoWrongClass) = 2.2011
Provides:       opt-perl(Moose::Exception::InstanceMustBeABlessedReference) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidArgPassedToMooseUtilMetaRole) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidArgumentToMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidArgumentsToTraitAliases) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidBaseTypeGivenToCreateParameterizedTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidHandleValue) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidHasProvidedInARole) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidNameForType) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidOverloadOperator) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidRoleApplication) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidTypeGivenToCreateParameterizedTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::InvalidValueForIs) = 2.2011
Provides:       opt-perl(Moose::Exception::IsaDoesNotDoTheRole) = 2.2011
Provides:       opt-perl(Moose::Exception::IsaLacksDoesMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::LazyAttributeNeedsADefault) = 2.2011
Provides:       opt-perl(Moose::Exception::Legacy) = 2.2011
Provides:       opt-perl(Moose::Exception::MOPAttributeNewNeedsAttributeName) = 2.2011
Provides:       opt-perl(Moose::Exception::MatchActionMustBeACodeRef) = 2.2011
Provides:       opt-perl(Moose::Exception::MessageParameterMustBeCodeRef) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassIsAClassNotASubclassOfGivenMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassIsARoleNotASubclassOfGivenMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassIsNotASubclassOfGivenMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassMustBeASubclassOfMooseMetaClass) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassMustBeASubclassOfMooseMetaRole) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassMustBeDerivedFromClassMOPClass) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassNotLoaded) = 2.2011
Provides:       opt-perl(Moose::Exception::MetaclassTypeIncompatible) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodExpectedAMetaclassObject) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodExpectsFewerArgs) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodExpectsMoreArgs) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodModifierNeedsMethodName) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodNameConflictInRoles) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodNameNotFoundInInheritanceHierarchy) = 2.2011
Provides:       opt-perl(Moose::Exception::MethodNameNotGiven) = 2.2011
Provides:       opt-perl(Moose::Exception::MustDefineAMethodName) = 2.2011
Provides:       opt-perl(Moose::Exception::MustDefineAnAttributeName) = 2.2011
Provides:       opt-perl(Moose::Exception::MustDefineAnOverloadOperator) = 2.2011
Provides:       opt-perl(Moose::Exception::MustHaveAtLeastOneValueToEnumerate) = 2.2011
Provides:       opt-perl(Moose::Exception::MustPassAHashOfOptions) = 2.2011
Provides:       opt-perl(Moose::Exception::MustPassAMooseMetaRoleInstanceOrSubclass) = 2.2011
Provides:       opt-perl(Moose::Exception::MustPassAPackageNameOrAnExistingClassMOPPackageInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::MustPassEvenNumberOfArguments) = 2.2011
Provides:       opt-perl(Moose::Exception::MustPassEvenNumberOfAttributeOptions) = 2.2011
Provides:       opt-perl(Moose::Exception::MustProvideANameForTheAttribute) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSpecifyAtleastOneMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSpecifyAtleastOneRole) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSpecifyAtleastOneRoleToApplicant) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyAClassMOPAttributeInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyADelegateToMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyAMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyAMooseMetaAttributeInstance) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyAnAccessorTypeToConstructWith) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyAnAttributeToConstructWith) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyArrayRefAsCurriedArguments) = 2.2011
Provides:       opt-perl(Moose::Exception::MustSupplyPackageNameAndName) = 2.2011
Provides:       opt-perl(Moose::Exception::NeedsTypeConstraintUnionForTypeCoercionUnion) = 2.2011
Provides:       opt-perl(Moose::Exception::NeitherAttributeNorAttributeNameIsGiven) = 2.2011
Provides:       opt-perl(Moose::Exception::NeitherClassNorClassNameIsGiven) = 2.2011
Provides:       opt-perl(Moose::Exception::NeitherRoleNorRoleNameIsGiven) = 2.2011
Provides:       opt-perl(Moose::Exception::NeitherTypeNorTypeNameIsGiven) = 2.2011
Provides:       opt-perl(Moose::Exception::NoAttributeFoundInSuperClass) = 2.2011
Provides:       opt-perl(Moose::Exception::NoBodyToInitializeInAnAbstractBaseClass) = 2.2011
Provides:       opt-perl(Moose::Exception::NoCasesMatched) = 2.2011
Provides:       opt-perl(Moose::Exception::NoConstraintCheckForTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::NoDestructorClassSpecified) = 2.2011
Provides:       opt-perl(Moose::Exception::NoImmutableTraitSpecifiedForClass) = 2.2011
Provides:       opt-perl(Moose::Exception::NoParentGivenToSubtype) = 2.2011
Provides:       opt-perl(Moose::Exception::OnlyInstancesCanBeCloned) = 2.2011
Provides:       opt-perl(Moose::Exception::OperatorIsRequired) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadConflictInSummation) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresAMetaClass) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresAMetaMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresAMetaOverload) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresAMethodNameOrCoderef) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresAnOperator) = 2.2011
Provides:       opt-perl(Moose::Exception::OverloadRequiresNamesForCoderef) = 2.2011
Provides:       opt-perl(Moose::Exception::OverrideConflictInComposition) = 2.2011
Provides:       opt-perl(Moose::Exception::OverrideConflictInSummation) = 2.2011
Provides:       opt-perl(Moose::Exception::PackageDoesNotUseMooseExporter) = 2.2011
Provides:       opt-perl(Moose::Exception::PackageNameAndNameParamsNotGivenToWrap) = 2.2011
Provides:       opt-perl(Moose::Exception::PackagesAndModulesAreNotCachable) = 2.2011
Provides:       opt-perl(Moose::Exception::ParameterIsNotSubtypeOfParent) = 2.2011
Provides:       opt-perl(Moose::Exception::ReferencesAreNotAllowedAsDefault) = 2.2011
Provides:       opt-perl(Moose::Exception::RequiredAttributeLacksInitialization) = 2.2011
Provides:       opt-perl(Moose::Exception::RequiredAttributeNeedsADefault) = 2.2011
Provides:       opt-perl(Moose::Exception::RequiredMethodsImportedByClass) = 2.2011
Provides:       opt-perl(Moose::Exception::RequiredMethodsNotImplementedByClass) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::Attribute) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::AttributeName) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::Class) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::EitherAttributeOrAttributeName) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::Instance) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::InstanceClass) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::InvalidAttributeOptions) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::Method) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::ParamsHash) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::Role) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::RoleForCreate) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::RoleForCreateMOPClass) = 2.2011
Provides:       opt-perl(Moose::Exception::Role::TypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::RoleDoesTheExcludedRole) = 2.2011
Provides:       opt-perl(Moose::Exception::RoleExclusionConflict) = 2.2011
Provides:       opt-perl(Moose::Exception::RoleNameRequired) = 2.2011
Provides:       opt-perl(Moose::Exception::RoleNameRequiredForMooseMetaRole) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesDoNotSupportAugment) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesDoNotSupportExtends) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesDoNotSupportInner) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesDoNotSupportRegexReferencesForMethodModifiers) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesInCreateTakesAnArrayRef) = 2.2011
Provides:       opt-perl(Moose::Exception::RolesListMustBeInstancesOfMooseMetaRole) = 2.2011
Provides:       opt-perl(Moose::Exception::SingleParamsToNewMustBeHashRef) = 2.2011
Provides:       opt-perl(Moose::Exception::TriggerMustBeACodeRef) = 2.2011
Provides:       opt-perl(Moose::Exception::TypeConstraintCannotBeUsedForAParameterizableType) = 2.2011
Provides:       opt-perl(Moose::Exception::TypeConstraintIsAlreadyCreated) = 2.2011
Provides:       opt-perl(Moose::Exception::TypeParameterMustBeMooseMetaType) = 2.2011
Provides:       opt-perl(Moose::Exception::UnableToCanonicalizeHandles) = 2.2011
Provides:       opt-perl(Moose::Exception::UnableToCanonicalizeNonRolePackage) = 2.2011
Provides:       opt-perl(Moose::Exception::UnableToRecognizeDelegateMetaclass) = 2.2011
Provides:       opt-perl(Moose::Exception::UndefinedHashKeysPassedToMethod) = 2.2011
Provides:       opt-perl(Moose::Exception::UnionCalledWithAnArrayRefAndAdditionalArgs) = 2.2011
Provides:       opt-perl(Moose::Exception::UnionTakesAtleastTwoTypeNames) = 2.2011
Provides:       opt-perl(Moose::Exception::ValidationFailedForInlineTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::ValidationFailedForTypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Exception::WrapTakesACodeRefToBless) = 2.2011
Provides:       opt-perl(Moose::Exception::WrongTypeConstraintGiven) = 2.2011
Provides:       opt-perl(Moose::Exporter) = 2.2011
Provides:       opt-perl(Moose::Intro) = 2.2011
Provides:       opt-perl(Moose::Manual) = 2.2011
Provides:       opt-perl(Moose::Manual::Attributes) = 2.2011
Provides:       opt-perl(Moose::Manual::BestPractices) = 2.2011
Provides:       opt-perl(Moose::Manual::Classes) = 2.2011
Provides:       opt-perl(Moose::Manual::Concepts) = 2.2011
Provides:       opt-perl(Moose::Manual::Construction) = 2.2011
Provides:       opt-perl(Moose::Manual::Contributing) = 2.2011
Provides:       opt-perl(Moose::Manual::Delegation) = 2.2011
Provides:       opt-perl(Moose::Manual::Delta) = 2.2011
Provides:       opt-perl(Moose::Manual::Exceptions) = 2.2011
Provides:       opt-perl(Moose::Manual::Exceptions::Manifest) = 2.2011
Provides:       opt-perl(Moose::Manual::FAQ) = 2.2011
Provides:       opt-perl(Moose::Manual::MOP) = 2.2011
Provides:       opt-perl(Moose::Manual::MethodModifiers) = 2.2011
Provides:       opt-perl(Moose::Manual::MooseX) = 2.2011
Provides:       opt-perl(Moose::Manual::Resources) = 2.2011
Provides:       opt-perl(Moose::Manual::Roles) = 2.2011
Provides:       opt-perl(Moose::Manual::Support) = 2.2011
Provides:       opt-perl(Moose::Manual::Types) = 2.2011
Provides:       opt-perl(Moose::Manual::Unsweetened) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Array) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Bool) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Code) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Counter) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Hash) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::Number) = 2.2011
Provides:       opt-perl(Moose::Meta::Attribute::Native::Trait::String) = 2.2011
Provides:       opt-perl(Moose::Meta::Class) = 2.2011
Provides:       opt-perl(Moose::Meta::Instance) = 2.2011
Provides:       opt-perl(Moose::Meta::Method) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Accessor) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Augmented) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Constructor) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Delegation) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Destructor) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Meta) = 2.2011
Provides:       opt-perl(Moose::Meta::Method::Overridden) = 2.2011
Provides:       opt-perl(Moose::Meta::Role) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Application) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Application::RoleSummation) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Application::ToClass) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Application::ToInstance) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Application::ToRole) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Attribute) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Composite) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Method) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Method::Conflicting) = 2.2011
Provides:       opt-perl(Moose::Meta::Role::Method::Required) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeCoercion) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeCoercion::Union) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Class) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::DuckType) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Enum) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Parameterizable) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Parameterized) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Registry) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Role) = 2.2011
Provides:       opt-perl(Moose::Meta::TypeConstraint::Union) = 2.2011
Provides:       opt-perl(Moose::Object) = 2.2011
Provides:       opt-perl(Moose::Role) = 2.2011
Provides:       opt-perl(Moose::Spec::Role) = 2.2011
Provides:       opt-perl(Moose::Unsweetened) = 2.2011
Provides:       opt-perl(Moose::Util) = 2.2011
Provides:       opt-perl(Moose::Util::MetaRole) = 2.2011
Provides:       opt-perl(Moose::Util::TypeConstraints) = 2.2011
Provides:       opt-perl(Test::Moose) = 2.2011
Provides:       opt-perl(metaclass) = 2.2011
Provides:       opt-perl(oose) = 2.2011
Requires:       opt-perl
Requires:       opt-perl(Devel::GlobalDestruction)
Requires:       opt-perl(Sub::Identify)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Devel::GlobalDestruction)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Sub::Identify)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Moose is an extension of the Perl 5 object system.

%prep

%setup  -n Moose-2.2011
chmod -R u+w %{_builddir}/Moose-%{version}

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
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 2.2011-1
- Generated using cpantorpm

