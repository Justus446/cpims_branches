from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from cpims_api import views

router = DefaultRouter()

router.register(' OVCBursaryViewSet'
router.register(' OVCCaseRecordViewSet'
router.register(' OVCCaseGeoViewSet'
router.register(' OVCEconomicStatusViewSet'
router.register(' OVCFamilyStatusViewSet'
router.register(' OVCHobbiesViewSet'
router.register(' OVCFriendsViewSet'
router.register(' OVCMedicalViewSet'
router.register(' OVCMedicalSubconditionsViewSet'
router.register(' OVCCaseCategoryViewSet'
router.register(' OVCCaseSubCategoryViewSet'
router.register(' OVCReferralViewSet'
# viewsets
router.register(' OVCPlacementViewSet'
router.register(' OVCCaseEventsViewSet'
router.register(' OVCCaseEventServicesViewSet'
router.register(' OVCCaseEventCourtViewSet'
router.register(' OVCCaseEventSummonViewSet'
router.register(' OVCCaseEventClosureViewSet'
router.register(' OVCRemindersViewSet'
router.register(' OVCDocumentsViewSet'
router.register(' OVCPlacementFollowUpViewSet'
router.register(' OVCDischargeFollowUpViewSet'
router.register(' OVCAdverseEventsFollowUpViewSet'
router.register(' OVCAdverseEventsOtherFollowUpViewSet'
router.register(' OVCFamilyCareViewSet'
router.register(' OVCCareEventsViewSet'
router.register(' OVCCareAssessmentViewSet'
router.register(' OVCCareEAVViewSet'
router.register(' OVCCareF1BViewSet'
router.register(' OVCGokBursaryViewSet'
router.register(' OVCCareFormsViewSet'
router.register(' OVCCareBenchmarkScoreViewSet'
router.register(' OVCCareWellbeingViewSet'
router.register(' OVCCareCasePlanViewSet'
router.register(' OVCHouseholdDemographicsViewSet'
router.register(' OVCExplanationsViewSet'
# viewsets
router.register(' OVCReferralsViewSet'
router.register(' OVCMonitoringViewSet'
router.register(' OVCMonitoring11ViewSet'
router.register(' OVCHivStatusViewSet'
router.register(' OVCHIVRiskScreeningViewSet'
router.register(' OVCHIVManagementViewSet'
# viewsets
router.register(' OVCBasicCRSViewSet'
router.register(' OVCBasicPersonViewSet'
router.register(' OVCBasicCategoryViewSet'
router.register(' OvcCasePersonsViewSet'
router.register(' OvcCaseInformationViewSet'
router.register(' OVCCaseLocationViewSet'
router.register(' OVCCareQuestionsViewSet'
router.register(' OVCCareCpara_upgradeViewSet'
router.register(' OVCSubPopulationViewSet'
router.register(' OVCCareIndividaulCparaViewSet'

router.register('persons_master', views.PersonsMasterViewSets   )
router.register('ovc_household', views.OVCHouseHoldViewSets   )
router.register('ovc_chekins', views.OVCCheckinViewSets   )
router.register('ovc_sibling', views.OVCSiblingViewSet   )
router.register('reg_person_audit_trail', views.RegPersonsAuditTrailViewSet)
router.register('reg_org_unit_audit_trail', views.RegOrgUnitsAuditTrailViewSet)
router.register('reg_person_benefiaciary', views.RegPersonsBeneficiaryIdsViewSet)
router.register('reg_person_workforce', views.RegPersonsWorkforceIdsViewSet)
router.register('reg_person_ou', views.RegPersonsOrgUnitsViewSet)
router.register('reg_person_contact', views.RegPersonsContactViewSet)
router.register('reg_person_external_ids', views.RegPersonsExternalIdsViewSet)
router.register('reg_person_geo', views.RegPersonsGeoViewSet)
router.register('reg_person_types', views.RegPersonsTypesViewSet)
router.register('reg_person_siblings', views.RegPersonsSiblingsViewSet)
router.register('reg_person_gurdians', views.RegPersonsGuardiansViewSet)
router.register('reg_biometric', views.RegBiometricViewSet)
router.register('reg_person', views.RegPersonViewSet)
router.register('reg_org_unit_geography', views.RegOrgUnitGeographyViewSet)
router.register('reg_org_unit_external_id', views.RegOrgUnitExternalIDViewSet)
router.register('reg_org_unit_contact', views.RegOrgUnitContactViewSet)
router.register('ovc_care_priorioty', views.OVCCarePriorityViewSet)
router.register('ovc_exit', views.OVCExitViewSet)
router.register('ovc_education_follow_up', views.OVCEducationFollowUpViewSet)
router.register('ovc_education_level_follow_up', views.OVCEducationLevelViewSet)
router.register('ovc_viral_load', views.OvcViralLoadViewSet)
router.register('ovc_care_services', views.OvcCareServicesViewSet)
router.register('school_list', views.SchoolListViewSet)
router.register('faciity_list', views.FacilityListViewSet)
router.register('reg_person', views.RegOrgUnitViewSet)
router.register('ovc_registration', views.OVCRegistrationViewSet)
router.register('reg_org_unit', views.RegOrgUnitViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('token-auth', obtain_auth_token, name='api_token_auth'),
]