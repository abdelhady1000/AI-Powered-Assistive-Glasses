from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    DISPID_SGRSTWeight, DISPID_SDKCreateKey,
    DISPIDSPTSI_SelectionOffset, SpeechTokenKeyUI, SAFT44kHz8BitMono,
    SRAInterpreter, ISpNotifySink, SP_VISEME_2, SVF_Emphasis,
    DISPID_SRCERequestUI, DISPID_SVIsUISupported, DISPID_SPPName,
    SASRun, DISPID_SVEStreamEnd, DISPID_SPIEngineId,
    DISPID_SRGIsPronounceable, SVEStartInputStream, SPAS_RUN,
    SAFT22kHz8BitMono, SVEPhoneme, DISPID_SVGetVoices,
    eLEXTYPE_PRIVATE3, SVSFParseMask, SAFT11kHz8BitMono,
    eLEXTYPE_PRIVATE9, DISPID_SASCurrentSeekPosition, DISPID_SVVolume,
    eLEXTYPE_PRIVATE20, DISPID_SRCCreateGrammar, SPWORDLIST,
    SPEI_TTS_BOOKMARK, eLEXTYPE_PRIVATE16, DISPID_SOTCSetId,
    DISPID_SRCVoice, DISPID_SPIProperties, SRCS_Disabled,
    ISpRecoGrammar, SP_VISEME_12, SVSFNLPSpeakPunc, SPEI_MIN_SR,
    DISPID_SRCRetainedAudioFormat, SDKLCurrentConfig, DISPID_SLPType,
    ISpeechGrammarRules, DISPID_SRGetFormat, ISpEventSink,
    SpResourceManager, _lcid, typelib_path, SVEEndInputStream,
    SpeechVoiceCategoryTTSRate, SPSHORTCUTPAIRLIST, dispid, SWTAdded,
    DISPID_SPEEngineConfidence, IInternetSecurityManager, SVP_18,
    SPGS_EXCLUSIVE, SRTStandard, SITooFast, CoClass, _RemotableHandle,
    eLEXTYPE_PRIVATE10, DISPID_SPRsItem, SPPS_Modifier, SPPS_Function,
    VARIANT, SPSNotOverriden, SpeechPropertyResponseSpeed,
    DISPID_SVEBookmark, DISPID_SGRsCommit, SAFT11kHz16BitStereo,
    STSF_FlagCreate, DISPID_SAFSetWaveFormatEx, DISPID_SPAs_NewEnum,
    SPEI_SR_BOOKMARK, DISPID_SRGCmdSetRuleIdState, SPVOICESTATUS,
    SPEI_MAX_TTS, DISPID_SLPPhoneIds, SPEVENT, ISpeechPhraseRules,
    DISPID_SRGCmdLoadFromMemory, DISPID_SRGRules, DISPID_SRIsShared,
    SREStateChange, SGPronounciation, DISPID_SRCreateRecoContext,
    DISPID_SRGDictationSetState, DISPID_SRRAlternates,
    ISpeechPhraseInfo, SVP_6, IEnumString, SAFTDefault,
    DISPID_SPRsCount, SAFT32kHz16BitMono, DISPID_SLPPartOfSpeech,
    SPRECORESULTTIMES, SSSPTRelativeToEnd, SPPS_Verb,
    DISPID_SRRecognizer, SpCompressedLexicon, SRTSMLTimeout,
    SECFNoSpecialChars, ISpResourceManager,
    DISPID_SGRSAddSpecialTransition, DISPID_SPERequiredConfidence,
    SPVPRI_OVER, Speech_Default_Weight, SPCS_DISABLED,
    eLEXTYPE_PRIVATE17, SVPAlert, DISPID_SAStatus,
    ISpeechLexiconPronunciation, Speech_StreamPos_Asap,
    SpeechAudioVolume, SpLexicon, SPINTERFERENCE_TOOFAST,
    DISPID_SRRDiscardResultInfo, DISPID_SREmulateRecognition,
    ISpObjectTokenCategory, SAFTNoAssignedFormat, SAFT48kHz8BitStereo,
    UINT_PTR, ISpeechXMLRecoResult, ISpeechWaveFormatEx,
    eLEXTYPE_PRIVATE5, SVP_1, SPSMF_SRGS_SAPIPROPERTIES, SVP_8,
    DISPID_SVVoice, SAFTCCITT_uLaw_44kHzMono, SPPS_LMA,
    SAFTCCITT_uLaw_22kHzStereo, SAFTCCITT_ALaw_8kHzStereo,
    DISPID_SAEventHandle, SPRST_NUM_STATES, ISpRecognizer,
    SPEI_REQUEST_UI, eLEXTYPE_PRIVATE2, DISPID_SOTsCount,
    SAFTExtendedAudioFormat, DISPID_SOTGetAttribute,
    ISpeechRecoResult, DISPID_SRCEHypothesis, SGDSActive,
    SpPhoneticAlphabetConverter, DISPID_SADefaultFormat,
    STSF_CommonAppData, SP_VISEME_1, SPBINARYGRAMMAR,
    ISpeechLexiconWord, DISPID_SASCurrentDevicePosition,
    DISPID_SRCSetAdaptationData, ISequentialStream, GUID,
    ISpeechAudioBufferInfo, DISPID_SPEs_NewEnum,
    SpeechDictationTopicSpelling, SREFalseRecognition, SDTRule,
    ISpeechLexiconPronunciations, DISPID_SAVolume, SVPOver,
    SAFTCCITT_uLaw_8kHzMono, SAFTCCITT_ALaw_11kHzStereo,
    DISPID_SCSBaseStream, SPINTERFERENCE_NOISE, SPEI_MAX_SR,
    DISPID_SRCERecognition, SPWT_LEXICAL_NO_SPECIAL_CHARS,
    DISPID_SRRSetTextFeedback, SpeechRegistryUserRoot,
    DISPID_SPPValue, ISpMMSysAudio, DISPID_SMSAMMHandle,
    SAFTCCITT_ALaw_44kHzStereo, SPEI_ACTIVE_CATEGORY_CHANGED,
    SPEI_PROPERTY_STRING_CHANGE, DISPID_SLAddPronunciationByPhoneIds,
    SPTEXTSELECTIONINFO, SPEI_SR_PRIVATE, DISPID_SVSpeakCompleteEvent,
    DISPIDSPTSI_SelectionLength, SPSInterjection,
    DISPID_SPIEnginePrivateData, eLEXTYPE_RESERVED7,
    ISpeechGrammarRuleStateTransition, SPPS_Noun, SGRSTTWildcard,
    SAFT12kHz16BitMono, DISPID_SLWLangId, SRTReSent,
    ISpeechPhraseReplacements, ISpeechVoice, DISPID_SRRTLength,
    SPEI_ADAPTATION, DISPID_SVSInputWordPosition, SPEI_HYPOTHESIS,
    SREPropertyStringChange, SPAO_NONE, SP_VISEME_14, SpMMAudioEnum,
    DISPID_SPPFirstElement, DISPID_SLWType, DISPID_SVAlertBoundary,
    SVPNormal, SDTProperty, DISPID_SVSLastResult, SRCS_Enabled,
    SSTTTextBuffer, SAFTADPCM_22kHzStereo, DISPID_SGRSTRule,
    DISPID_SDKGetBinaryValue, SAFTCCITT_uLaw_44kHzStereo,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, SPBO_AHEAD,
    DISPID_SRGCmdSetRuleState, SREInterference,
    DISPID_SPEAudioSizeTime, SVSFPurgeBeforeSpeak,
    DISPID_SVAudioOutput, DISPID_SVResume, SREAllEvents,
    DISPID_SRCBookmark, IStream, DISPID_SASetState, SPFM_CREATE,
    DISPID_SPRuleParent, ISpeechRecoResultTimes, ISpVoice,
    ISpRecognizer3, SRSActive, SPEI_RESERVED6, SPSVerb,
    SPPHRASEREPLACEMENT, SLOStatic, DISPID_SPERetainedStreamOffset,
    DISPID_SRCCreateResultFromMemory, SDA_Consume_Leading_Spaces,
    SECFIgnoreWidth, DISPID_SRSetPropertyString,
    DISPID_SVESentenceBoundary, SAFT24kHz16BitStereo, SVP_10,
    DISPID_SABIMinNotification, ISpNotifySource, SPVPRI_NORMAL,
    ISpeechObjectTokenCategory, ISpeechObjectTokens,
    ISpSerializeState, STCLocalServer, SVF_None, ISpPhraseAlt,
    DISPID_SABIBufferSize, tagSTATSTG, SpeechAudioFormatGUIDWave,
    SRSEDone, DISPID_SRCRequestedUIType, DISPIDSPTSI_ActiveOffset,
    DISPID_SOTCDefault, SGRSTTDictation, SPEI_PHONEME, SP_VISEME_20,
    SECFDefault, SP_VISEME_17, SVSFIsXML, DISPID_SRState,
    DISPID_SDKSetBinaryValue, SWPKnownWordPronounceable,
    eLEXTYPE_PRIVATE8, SP_VISEME_18, SVSFVoiceMask,
    SECFIgnoreKanaType, SDTReplacement, DISPID_SPAsCount,
    SP_VISEME_11, COMMETHOD, DISPID_SMSADeviceId, SDTDisplayText,
    SVEVoiceChange, SPRST_INACTIVE_WITH_PURGE, SVP_19,
    SpeechTokenIdUserLexicon, DISPID_SVEWord,
    DISPID_SRRGetXMLErrorInfo, ISpeechResourceLoader,
    DISPID_SPIElements, SVSFIsFilename, DISPID_SVWaitUntilDone,
    SPEI_UNDEFINED, SPEI_TTS_AUDIO_LEVEL, DISPID_SGRSTText,
    DISPID_SGRSTs_NewEnum, SpObjectToken, DISPID_SBSFormat,
    DISPID_SPRuleConfidence, SDKLCurrentUser,
    DISPID_SVSLastBookmarkId, STCRemoteServer, SPEI_VISEME,
    DISPID_SBSWrite, DISPID_SPAStartElementInResult, DISPID_SOTSetId,
    ISpProperties, SGLexical, Speech_Max_Pron_Length,
    DISPID_SGRsCount, ISpeechPhraseProperties, DISPID_SLGenerationId,
    SPAUDIOBUFFERINFO, DISPID_SWFEBlockAlign, DISPID_SVSPhonemeId,
    SDA_Two_Trailing_Spaces, SVP_9, SpeechVoiceSkipTypeSentence,
    DISPID_SPRuleChildren, DISPID_SVSpeakStream, SAFT32kHz8BitMono,
    SpInProcRecoContext, SPPS_RESERVED3, SpStream,
    SPXRO_Alternates_SML, SAFT16kHz16BitMono,
    SpeechRegistryLocalMachineRoot, SPSHT_Unknown, SPWT_LEXICAL,
    SPWF_SRENGINE, ISpeechAudio, DISPID_SRRSpeakAudio,
    DISPID_SLWs_NewEnum, ISpeechCustomStream,
    DISPID_SPERetainedSizeBytes, ISpRecoContext,
    DISPID_SGRSTPropertyName, SAFTADPCM_11kHzStereo,
    DISPID_SPRulesCount, SAFTADPCM_11kHzMono, DISPID_SPPParent,
    SPPS_RESERVED2, eLEXTYPE_PRIVATE18, SPEI_VOICE_CHANGE,
    SPSHT_EMAIL, SAFT44kHz16BitMono, tagSPTEXTSELECTIONINFO,
    SFTSREngine, DISPID_SABufferInfo, DISPID_SPRuleId,
    DISPID_SVSCurrentStreamNumber, SAFT16kHz16BitStereo, SRERequestUI,
    SpeechTokenKeyAttributes, SLTApp, ISpeechVoiceStatus,
    DISPID_SMSALineId, DISPID_SVStatus, DISPID_SOTCreateInstance,
    DISPID_SRCEAudioLevel, DISPID_SABIEventBias, DISPID_SVSkip,
    SPWT_PRONUNCIATION, DISPID_SOTDisplayUI, DISPID_SLPLangId,
    SPRST_ACTIVE_ALWAYS, SpeechCategoryAudioIn, SPVPRI_ALERT,
    DISPID_SVGetProfiles, DISPID_SOTCategory, DISPID_SVEViseme,
    SPEI_START_INPUT_STREAM, DISPID_SFSClose, DISPID_SPELexicalForm,
    SPSMF_SAPI_PROPERTIES, ISpeechGrammarRule, STSF_LocalAppData,
    ISpStreamFormat, STCInprocServer, SAFT32kHz16BitStereo,
    DISPID_SWFEExtraData, DISPID_SOTRemoveStorageFileName,
    DISPID_SLGetGenerationChange, SPBO_PAUSE,
    DISPID_SPPNumberOfElements, SPEI_SR_AUDIO_LEVEL, SP_VISEME_13,
    SPBO_TIME_UNITS, ISpeechPhraseElement, SAFTGSM610_8kHzMono,
    DISPID_SVEVoiceChange, SPCT_DICTATION, DISPID_SRIsUISupported,
    SpeechCategoryPhoneConverters, SSTTWildcard, SPPHRASEPROPERTY,
    SBOPause, ISpeechRecoResult2, SPAUDIOSTATUS, ISpStream,
    eLEXTYPE_APP, SSFMOpenForRead, SpFileStream, DISPID_SOTRemove,
    SPLO_DYNAMIC, ISpGrammarBuilder, SGRSTTRule,
    SPINTERFERENCE_LATENCY_WARNING, ISpeechDataKey,
    ISpeechMemoryStream, SSFMCreateForWrite, DISPID_SRRTStreamTime,
    SAFT32kHz8BitStereo, DISPID_SRCRetainedAudio, SASClosed,
    DISPID_SRGCmdLoadFromFile, DISPID_SPRuleEngineConfidence,
    SPAS_CLOSED, SDA_One_Trailing_Space, SPDKL_DefaultLocation,
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE, SPPHRASERULE, SPRST_ACTIVE,
    DISPID_SRCPause, ISpeechTextSelectionInformation,
    SVSFParseAutodetect, _check_version,
    DISPID_SVSyncronousSpeakTimeout, SPFM_OPEN_READWRITE,
    eLEXTYPE_LETTERTOSOUND, SpMMAudioIn, DISPID_SPEAudioStreamOffset,
    SAFT24kHz8BitStereo, SPEI_END_SR_STREAM, ISpeechLexicon,
    SPSERIALIZEDPHRASE, SpVoice, DISPID_SDKDeleteKey,
    DISPID_SGRSTsCount, SREPrivate, SPEVENTSOURCEINFO,
    SpPhoneConverter, eLEXTYPE_PRIVATE7, DISPID_SPEAudioTimeOffset,
    SAFTCCITT_ALaw_11kHzMono, DISPID_SGRId, SINoSignal,
    SAFT8kHz16BitStereo, SPCS_ENABLED, SPEI_RESERVED3,
    DISPID_SRCCmdMaxAlternates, SPINTERFERENCE_NONE, SGSExclusive,
    SPEI_INTERFERENCE, DISPID_SPRuleFirstElement,
    DISPID_SGRSTPropertyValue, ISpObjectWithToken,
    SpeechPropertyLowConfidenceThreshold, DISPID_SLPSymbolic,
    SPSERIALIZEDRESULT, SGRSTTEpsilon, DISPID_SPILanguageId,
    SP_VISEME_16, DISPID_SOTDataKey, SpeechPropertyResourceUsage,
    SAFTCCITT_uLaw_11kHzStereo, DISPID_SRCESoundStart,
    SAFTCCITT_ALaw_44kHzMono, SpeechAudioProperties,
    DISPID_SRGCmdLoadFromProprietaryGrammar, SAFT44kHz16BitStereo,
    SAFT16kHz8BitMono, SPFM_OPEN_READONLY, DISPID_SGRSRule,
    SRATopLevel, DISPID_SABufferNotifySize, DISPID_SPEDisplayText,
    SWPUnknownWordPronounceable, SWTDeleted, SpeechTokenKeyFiles,
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, eLEXTYPE_RESERVED10,
    SSFMCreate, STSF_AppData, SPEI_SOUND_END, SGDisplay,
    SPRST_INACTIVE, ISpeechAudioStatus, DISPID_SVSInputSentenceLength,
    SDTLexicalForm, _ISpeechRecoContextEvents, SVP_20,
    ISpeechPhraseAlternate, SPSHORTCUTPAIR, SpeechAddRemoveWord,
    ISpeechRecoContext, Speech_StreamPos_RealTime,
    ISpPhoneticAlphabetSelection, eLEXTYPE_MORPHOLOGY, DISPID_SGRName,
    DISPID_SPIRetainedSizeBytes, SAFTGSM610_22kHzMono, DISPID_SBSSeek,
    SPWORD, DISPID_SLPsItem, DISPID_SRCEEnginePrivate,
    SpNotifyTranslator, SGDSInactive, SVEViseme,
    DISPID_SPEDisplayAttributes, DISPID_SRSNumberOfActiveRules,
    DISPID_SPRuleNumberOfElements, SRTExtendableParse,
    DISPID_SRGState, SPEI_PROPERTY_NUM_CHANGE,
    SpeechGrammarTagUnlimitedDictation, SREPropertyNumChange,
    SDA_No_Trailing_Space, DISPID_SPRs_NewEnum,
    DISPID_SRSetPropertyNumber, SVEPrivate, SPEI_FALSE_RECOGNITION,
    SDTPronunciation, SpTextSelectionInformation,
    SPEI_SENTENCE_BOUNDARY, SpAudioFormat, DISPID_SRGRecoContext,
    SPSSuppressWord, SPAR_High, SVSFPersistXML,
    SAFTCCITT_ALaw_22kHzStereo, DISPID_SASFreeBufferSpace,
    DISPID_SPEsCount, SpeechUserTraining, SVP_14, SVP_21,
    DISPID_SRCEBookmark, DISPID_SPACommit,
    DISPID_SPPBRestorePhraseFromMemory, DISPID_SGRAddState,
    eLEXTYPE_RESERVED4, DISPID_SGRsDynamic, DISPID_SPIAudioSizeTime,
    SPCT_COMMAND, SDKLDefaultLocation, DISPID_SGRs_NewEnum,
    DISPID_SPIGrammarId, DISPID_SGRsCommitAndSave, SRTEmulated,
    ISpeechRecognizer, SAFTADPCM_8kHzMono, DISPID_SRAudioInput,
    DISPID_SRRTOffsetFromStart, DISPID_SAFType,
    DISPID_SRGDictationLoad, _ULARGE_INTEGER,
    SpeechCategoryRecoProfiles,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, SPDKL_LocalMachine,
    SPEI_RECOGNITION, eLEXTYPE_PRIVATE15, DISPID_SDKEnumValues,
    SPINTERFERENCE_TOOSLOW, DISPID_SVDisplayUI, SP_VISEME_19,
    SPPS_NotOverriden, DISPID_SPRDisplayAttributes,
    SAFT22kHz8BitStereo, SPGS_DISABLED, SBONone, SVSFParseSsml, SVP_4,
    IServiceProvider, SPSMF_SRGS_SEMANTICINTERPRETATION_W3C,
    DISPID_SRCEEndStream, DISPID_SDKOpenKey, SFTInput,
    DISPID_SPEsItem, SRERecognition, SRSInactive,
    ISpeechPhoneConverter, DISPID_SRCResume, SAFTText,
    STCInprocHandler, SPRULE, DISPID_SPRuleName, SPSModifier,
    ISpRecoResult, SGRSTTTextBuffer,
    DISPID_SRCERecognitionForOtherContext, SVEWordBoundary,
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS, DISPID_SVEEnginePrivate,
    WSTRING, SREHypothesis, DISPID_SPIGetDisplayAttributes,
    DISPID_SRCVoicePurgeEvent, DISPID_SLPsCount, SP_VISEME_15,
    SAFT8kHz8BitStereo, SpMMAudioOut, DISPID_SRRTTickCount, _FILETIME,
    SpObjectTokenCategory, DISPID_SRSCurrentStreamNumber,
    IInternetSecurityMgrSite, SINoise, DISPID_SPRFirstElement,
    SPSFunction, DISPID_SDKGetStringValue, SREAdaptation,
    DISPID_SRSClsidEngine, SVP_17, DISPID_SRSAudioStatus,
    ISpeechPhraseInfoBuilder, DISPID_SVSpeak,
    ISpeechGrammarRuleStateTransitions, ISpPhoneConverter,
    SPEI_RESERVED2, SRAORetainAudio, DISPID_SRCEFalseRecognition,
    SPINTERFERENCE_TOOLOUD, SITooSlow, DISPID_SRCState,
    DISPID_SLAddPronunciation, SVP_15, SPSHT_NotOverriden, SPSMF_UPS,
    SRAExport, DISPID_SPRules_NewEnum, SP_VISEME_21,
    DISPIDSPTSI_ActiveLength, eLEXTYPE_RESERVED8, DISPID_SLWsCount,
    eLEXTYPE_USER_SHORTCUT, SAFTGSM610_11kHzMono, SVEBookmark,
    SpCustomStream, SECFIgnoreCase, Speech_Max_Word_Length,
    DISPID_SGRSTType, SVP_5, SpUnCompressedLexicon,
    __MIDL___MIDL_itf_sapi_0000_0020_0002,
    SpeechPropertyComplexResponseSpeed, eLEXTYPE_PRIVATE14,
    SGLexicalNoSpecialChars, eWORDTYPE_ADDED, SpSharedRecognizer,
    SREAudioLevel, DISPID_SRGSetWordSequenceData, SVP_13,
    SPEI_RECO_STATE_CHANGE, DISPID_SRCERecognizerStateChange,
    DISPID_SRCEInterference, ISpeechObjectToken, SDTAudio,
    SpeechCategoryAppLexicons, SPINTERFERENCE_NOSIGNAL,
    DISPID_SMSSetData, SPRECOCONTEXTSTATUS, SVEAllEvents,
    SpSharedRecoContext, SINone, SpNullPhoneConverter, SPSLMA,
    DISPID_SPPs_NewEnum, DISPID_SLRemovePronunciationByPhoneIds,
    DISPID_SRGetPropertyString, SPRS_INACTIVE, IUnknown, SP_VISEME_9,
    SpeechTokenValueCLSID, ISpeechGrammarRuleState, SASPause,
    SPFM_NUM_MODES, SpeechPropertyAdaptationOn, SPWT_DISPLAY,
    SpeechGrammarTagWildcard, SPRECOGNIZERSTATUS,
    __MIDL_IWinTypes_0009, ISpeechPhraseRule, WAVEFORMATEX,
    SSSPTRelativeToCurrentPosition, SAFT12kHz16BitStereo, DISPMETHOD,
    SPDKL_CurrentUser, DISPID_SWFESamplesPerSec, ISpeechBaseStream,
    DISPID_SOTIsUISupported, SVEAudioLevel,
    DISPID_SPRNumberOfElements, DISPID_SPIRule, DISPID_SLWsItem,
    ISpeechMMSysAudio, ISpeechRecognizerStatus, SRAONone,
    ISpXMLRecoResult, ISpObjectToken, SPAR_Low, SpeechAllElements,
    SpeechCategoryAudioOut, ISpeechRecoResultDispatch, DISPID_SLWWord,
    SRAImport, SpeechCategoryVoices, DISPID_SGRsAdd,
    DISPID_SVSInputSentencePosition, SECHighConfidence,
    SPEI_RESERVED5, SPCT_SUB_COMMAND, SPGS_ENABLED,
    DISPID_SDKSetLongValue, wireHWND, ISpeechLexiconWords,
    SWPUnknownWordUnpronounceable, SAFTCCITT_ALaw_22kHzMono,
    DISPID_SWFEChannels, ISpAudio, DISPID_SOTMatchesAttributes,
    DISPID_SPIGetText, SPAS_STOP, DISPID_SRRRecoContext,
    DISPID_SRGCmdLoadFromResource, SAFT8kHz16BitMono,
    SPCT_SUB_DICTATION, DISPID_SPEAudioSizeBytes, SPAS_PAUSE,
    DISPID_SRSSupportedLanguages, SAFTCCITT_uLaw_22kHzMono,
    SAFT48kHz16BitMono, DISPID_SGRClear, SITooQuiet,
    SPSEMANTICERRORINFO, DISPID_SGRSAddRuleTransition,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet, ISpShortcut,
    eLEXTYPE_USER, SPAO_RETAIN_AUDIO, DISPID_SVSRunningState,
    ISpeechFileStream, SVSFlagsAsync, DISPID_SVEStreamStart,
    SP_VISEME_7, SpeechGrammarTagDictation, SPEI_RESERVED1,
    SSTTDictation, ISpRecognizer2, DISPID_SGRSTransitions,
    SpPhraseInfoBuilder, SVSFDefault, DISPID_SPRulesItem, Library,
    SGSDisabled, DISPID_SLPs_NewEnum, DISPID_SPEActualConfidence,
    SSFMOpenReadWrite, SECNormalConfidence, SLTUser, DISPID_SPCLangId,
    DISPID_SOTCGetDataKey, SPEI_PHRASE_START, SPWF_INPUT,
    SPAR_Unknown, eLEXTYPE_VENDORLEXICON, SVP_0,
    DISPID_SVSLastBookmark, SRSActiveAlways,
    DISPID_SRGDictationUnload, DISPID_SFSOpen, SVP_3,
    SPRS_ACTIVE_USER_DELIMITED, SPPS_SuppressWord,
    DISPID_SRCAudioInInterferenceStatus, SPCT_SLEEP, SVSFNLPMask,
    DISPID_SPISaveToMemory, DISPID_SVEAudioLevel, ISpNotifyTranslator,
    ISpeechRecoGrammar, DISPID_SGRSTsItem, DISPID_SRRAudio, SPXRO_SML,
    SRSEIsSpeaking, DISPID_SOTGetStorageFileName, SAFT12kHz8BitMono,
    DISPID_SPAPhraseInfo, SAFT8kHz8BitMono, SPPS_RESERVED1,
    DISPID_SLWPronunciations, DISPID_SWFEAvgBytesPerSec, SPPS_Unknown,
    DISPID_SDKGetlongValue, SAFT22kHz16BitMono, DISPID_SOTs_NewEnum,
    SDTAll, SAFTADPCM_22kHzMono, _LARGE_INTEGER, SPPS_Noncontent,
    SPDKL_CurrentConfig, DISPID_SAFGetWaveFormatEx, SpeechMicTraining,
    DISPID_SGRsFindRule, DISPID_SVAudioOutputStream, ISpDataKey,
    DISPID_SLGetPronunciations, DISPID_SRRPhraseInfo,
    SDKLLocalMachine, DISPID_SRCESoundEnd, DISPID_SRGReset,
    DISPID_SPPChildren, SAFTTrueSpeech_8kHz1BitMono,
    SPFM_CREATE_ALWAYS, SPSNoun, SAFTNonStandardFormat,
    SpeechAudioFormatGUIDText, SECFEmulateResult,
    DISPID_SPEPronunciation, tagSPPROPERTYINFO, SPEI_SR_RETAINEDAUDIO,
    DISPID_SPAsItem, DISPID_SRCEPhraseStart, DISPID_SRDisplayUI,
    SPEI_TTS_PRIVATE, DISPID_SVSLastStreamNumberQueued, SVP_2,
    ISpStreamFormatConverter, SpeechPropertyHighConfidenceThreshold,
    eLEXTYPE_PRIVATE13, helpstring, DISPID_SGRSTPropertyId,
    IEnumSpObjectTokens, DISPID_SOTsItem, ISpeechPhraseAlternates,
    DISPID_SVPause, DISPID_SVSInputWordLength, SPEI_SOUND_START,
    SPEI_START_SR_STREAM, SPWORDPRONUNCIATIONLIST,
    ISpeechPhraseReplacement, DISPID_SPPEngineConfidence, SP_VISEME_0,
    SVSFIsNotXML, SPPS_RESERVED4, DISPID_SRGId, SVP_7,
    SPWORDPRONUNCIATION, SREBookmark, SPAR_Medium, DISPID_SRGCommit,
    DISPID_SVRate, DISPID_SPPsCount, SVP_16, DISPID_SRProfile,
    SpShortcut, DISPID_SOTCEnumerateTokens, DISPID_SDKSetStringValue,
    BSTR, SAFTCCITT_ALaw_8kHzMono, DISPID_SRGetRecognizers,
    SRESoundEnd, SDTAlternates, SPINTERFERENCE_TOOQUIET, SP_VISEME_10,
    eLEXTYPE_PRIVATE12, SAFTADPCM_44kHzMono, SITooLoud, SPEI_MIN_TTS,
    SREStreamEnd, SpWaveFormatEx, DISPID_SPIStartTime,
    DISPID_SRCRecognizer, SP_VISEME_8, eLEXTYPE_PRIVATE4,
    DISPID_SASNonBlockingIO, ISpRecoContext2, SAFT16kHz8BitStereo,
    DISPID_SRAudioInputStream, SPBO_NONE, SAFTCCITT_uLaw_11kHzMono,
    DISPID_SRRAudioFormat, SRADefaultToActive,
    __MIDL___MIDL_itf_sapi_0000_0020_0001, DISPID_SPCIdToPhone,
    eLEXTYPE_RESERVED6, eLEXTYPE_PRIVATE6, SpStreamFormatConverter,
    SPPROPERTYINFO, SpeechEngineProperties, DISPID_SGRSTNextState,
    SAFTADPCM_44kHzStereo, ISpRecoCategory, SPEI_RECO_OTHER_CONTEXT,
    DISPID_SPANumberOfElementsInResult, DISPID_SGRInitialState,
    DISPID_SVGetAudioOutputs, SVESentenceBoundary, DISPID_SPPsItem,
    SPEI_WORD_BOUNDARY, SAFT12kHz8BitStereo, DISPID_SGRAddResource,
    DISPID_SRCEStartStream, SAFT24kHz8BitMono, DISPID_SASState,
    DISPID_SPCPhoneToId, SpMemoryStream, DISPID_SOTCId, SRTAutopause,
    DISPID_SRGSetTextSelection, SPRS_ACTIVE,
    SPINTERFERENCE_LATENCY_TRUNCATE_END, DISPID_SPIReplacements,
    SSSPTRelativeToStart, SAFTGSM610_44kHzMono, SGRSTTWord,
    eLEXTYPE_PRIVATE1, DISPID_SMSGetData, SpeechRecoProfileProperties,
    SAFTADPCM_8kHzStereo, DISPID_SOTGetDescription, SVSFParseSapi,
    ISpeechPhraseProperty, DISPID_SLGetWords, eLEXTYPE_PRIVATE11,
    DISPID_SRCEPropertyStringChange, DISPID_SGRSAddWordTransition,
    SpInprocRecognizer, SPSHT_OTHER, DISPID_SRSCurrentStreamPosition,
    eLEXTYPE_PRIVATE19, SRESoundStart,
    SpeechPropertyNormalConfidenceThreshold, eLEXTYPE_RESERVED9,
    SREStreamStart, DISPID_SPARecoResult, SGDSActiveWithAutoPause,
    SASStop, SVSFUnusedFlags, DISPID_SBSRead, DISPID_SRStatus,
    SRARoot, SAFT44kHz8BitStereo, SRSInactiveWithPurge,
    ISpPhoneticAlphabetConverter, DISPID_SAFGuid, SAFT24kHz16BitMono,
    SRADynamic, DISPID_SRGetPropertyNumber,
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN,
    DISPID_SRCEPropertyNumberChange, DISPID_SWFEFormatTag,
    DISPID_SOTId, SPRS_ACTIVE_WITH_AUTO_PAUSE, STCAll,
    eWORDTYPE_DELETED, DISPID_SPIAudioStreamPosition,
    DISPID_SRCEventInterests, DISPID_SPPConfidence,
    SAFT48kHz16BitStereo, DISPID_SVGetAudioInputs, DISPID_SPRText,
    SP_VISEME_4, ISpPhrase, DISPID_SVSVisemeId, DISPID_SGRsItem,
    SPSUnknown, _ISpeechVoiceEvents, DISPID_SGRAttributes,
    SGDSActiveUserDelimited, DISPID_SRGCmdLoadFromObject,
    SPEI_END_INPUT_STREAM, SpeechCategoryRecognizers, SPPHRASEELEMENT,
    DISPID_SPIAudioSizeBytes, SPLO_STATIC, DISPID_SRCEAdaptation,
    SECLowConfidence, DISPID_SVEventInterests, ISpeechAudioFormat,
    DISPID_SRRSaveToMemory, SAFT48kHz8BitMono, SPPS_Interjection,
    SREPhraseStart, SVP_11, SPPHRASE, SAFT22kHz16BitStereo,
    ISpeechPhraseElements, LONG_PTR, SVF_Stressed,
    DISPID_SRRGetXMLResult, DISPID_SWFEBitsPerSample, HRESULT,
    SAFT11kHz16BitMono, SRERecoOtherContext, DISPID_SDKDeleteValue,
    SGSEnabled, DISPID_SLRemovePronunciation, DISPID_SPPId,
    SAFT11kHz8BitStereo, ULONG_PTR, SLODynamic, SP_VISEME_5, SVP_12,
    DISPID_SDKEnumKeys, DISPID_SVPriority, SAFTCCITT_uLaw_8kHzStereo,
    DISPID_SVEPhoneme, SP_VISEME_3, SP_VISEME_6, DISPID_SRRTimes,
    ISpRecoGrammar2, VARIANT_BOOL, ISpLexicon, ISpEventSource,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet
)


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class SpeechVoiceSpeakFlags(IntFlag):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class SpeechAudioFormatType(IntFlag):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SPPARTOFSPEECH(IntFlag):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPLEXICONTYPE(IntFlag):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechPartOfSpeech(IntFlag):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE
SPAUDIOSTATE = _SPAUDIOSTATE


__all__ = [
    'DISPID_SGRSTWeight', 'DISPID_SDKCreateKey',
    'DISPIDSPTSI_SelectionOffset', 'SDTPronunciation',
    'SpTextSelectionInformation', 'SPEI_SENTENCE_BOUNDARY',
    'SpAudioFormat', 'DISPID_SRGRecoContext', 'SpeechTokenKeyUI',
    'SAFT44kHz8BitMono', 'SRAInterpreter', 'SPSSuppressWord',
    'ISpNotifySink', 'SP_VISEME_2', 'SPAR_High', 'SVSFPersistXML',
    'SVF_Emphasis', 'DISPID_SRCERequestUI', 'DISPID_SVIsUISupported',
    'DISPID_SPPName', 'DISPID_SpeechPhraseAlternates', 'SASRun',
    'SAFTCCITT_ALaw_22kHzStereo', 'DISPID_SASFreeBufferSpace',
    'DISPID_SVEStreamEnd', 'DISPID_SPEsCount', 'SpeechUserTraining',
    'SVP_14', 'SVP_21', 'DISPID_SRCEBookmark', 'DISPID_SPIEngineId',
    'DISPID_SRGIsPronounceable', 'DISPID_SPACommit',
    'DISPID_SPPBRestorePhraseFromMemory', 'SPBOOKMARKOPTIONS',
    'SVEStartInputStream', 'DISPID_SGRAddState', 'SPDATAKEYLOCATION',
    'SAFT22kHz8BitMono', 'SPAS_RUN', 'DISPID_SGRsDynamic',
    'eLEXTYPE_RESERVED4', 'DISPID_SPIAudioSizeTime', 'SVEPhoneme',
    'SPCT_COMMAND', 'DISPID_SpeechGrammarRules', 'DISPID_SVGetVoices',
    'SDKLDefaultLocation', 'DISPID_SGRs_NewEnum',
    'DISPID_SPIGrammarId', 'DISPID_SGRsCommitAndSave',
    'eLEXTYPE_PRIVATE3', 'SVSFParseMask', 'SAFT11kHz8BitMono',
    'SRTEmulated', 'ISpeechRecognizer', 'eLEXTYPE_PRIVATE9',
    'DISPID_SASCurrentSeekPosition', 'DISPID_SVVolume',
    'eLEXTYPE_PRIVATE20', 'DISPID_SRCCreateGrammar', 'SPWORDLIST',
    'SPEI_TTS_BOOKMARK', 'SAFTADPCM_8kHzMono', 'DISPID_SRAudioInput',
    'eLEXTYPE_PRIVATE16', 'SPSEMANTICFORMAT', 'DISPID_SOTCSetId',
    'DISPID_SpeechPhraseReplacements', 'DISPID_SRRTOffsetFromStart',
    'DISPID_SRCVoice', 'DISPID_SAFType', 'DISPID_SPIProperties',
    'DISPID_SRGDictationLoad', 'SpeechCategoryRecoProfiles',
    'SRCS_Disabled', 'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'SPDKL_LocalMachine', 'ISpRecoGrammar', 'SP_VISEME_12',
    'SVSFNLPSpeakPunc', 'SPEI_RECOGNITION', 'SPEI_MIN_SR',
    'DISPID_SRCRetainedAudioFormat', 'eLEXTYPE_PRIVATE15',
    'SDKLCurrentConfig', 'DISPID_SLPType', 'ISpeechGrammarRules',
    'DISPID_SDKEnumValues', 'DISPID_SRGetFormat',
    'SPINTERFERENCE_TOOSLOW', 'DISPID_SVDisplayUI',
    'SpResourceManager', 'SP_VISEME_19', 'SPPS_NotOverriden',
    'DISPID_SPRDisplayAttributes', 'ISpEventSink', 'typelib_path',
    'DISPID_SpeechXMLRecoResult', 'SAFT22kHz8BitStereo',
    'SPGS_DISABLED', 'SBONone', 'SVSFParseSsml', 'SVP_4',
    'SVEEndInputStream', 'SpeechVoiceCategoryTTSRate',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C', 'DISPID_SRCEEndStream',
    'DISPID_SDKOpenKey', 'SFTInput', 'DISPID_SPEsItem',
    'SRERecognition', 'SRSInactive', 'SPSHORTCUTPAIRLIST', 'SWTAdded',
    'ISpeechPhoneConverter', 'DISPID_SPEEngineConfidence',
    'IInternetSecurityManager', 'DISPID_SRCResume', 'SAFTText',
    'STCInprocHandler', 'SPGS_EXCLUSIVE', 'SRTStandard', 'SVP_18',
    'DISPID_SPRuleName', 'SPRULE', 'SPSModifier', 'ISpRecoResult',
    'SGRSTTTextBuffer', 'DISPID_SRCERecognitionForOtherContext',
    'SITooFast', '_RemotableHandle', 'eLEXTYPE_PRIVATE10',
    'DISPID_SPRsItem', 'SPPS_Modifier', 'SVEWordBoundary',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_MS', 'DISPID_SVEEnginePrivate',
    'SPPS_Function', 'SPSNotOverriden', 'SpeechPartOfSpeech',
    'SpeechPropertyResponseSpeed', 'SREHypothesis',
    'DISPID_SPIGetDisplayAttributes', 'DISPID_SVEBookmark',
    'DISPID_SRCVoicePurgeEvent', 'DISPID_SLPsCount', 'SP_VISEME_15',
    'SAFT8kHz8BitStereo', 'DISPID_SGRsCommit',
    'SpeechGrammarRuleStateTransitionType', 'SpMMAudioOut',
    'DISPID_SRRTTickCount', 'SAFT11kHz16BitStereo', 'STSF_FlagCreate',
    'DISPID_SpeechCustomStream', 'SPWAVEFORMATTYPE',
    'DISPID_SAFSetWaveFormatEx', 'DISPID_SPAs_NewEnum',
    'SpObjectTokenCategory', 'SPEI_SR_BOOKMARK',
    'DISPID_SRGCmdSetRuleIdState', 'DISPID_SpeechGrammarRuleState',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SPVOICESTATUS',
    'DISPID_SRSCurrentStreamNumber', 'IInternetSecurityMgrSite',
    'SPEI_MAX_TTS', 'SpeechTokenShellFolder', 'DISPID_SLPPhoneIds',
    'SPEVENT', 'SpeechRuleState', 'SINoise', 'SPCONTEXTSTATE',
    'ISpeechPhraseRules', 'DISPID_SRGCmdLoadFromMemory',
    'DISPID_SPRFirstElement', 'DISPID_SRGRules', 'DISPID_SRIsShared',
    'DISPID_SDKGetStringValue', 'SPSFunction', 'SGPronounciation',
    'SREStateChange', 'SREAdaptation', 'DISPID_SRSClsidEngine',
    'SVP_17', 'DISPID_SRSAudioStatus', 'ISpeechPhraseInfoBuilder',
    'DISPID_SRCreateRecoContext', 'DISPID_SVSpeak',
    'ISpeechGrammarRuleStateTransitions',
    'DISPID_SRGDictationSetState', 'SPEI_RESERVED2',
    'DISPID_SRRAlternates', 'ISpeechPhraseInfo', 'SVP_6',
    'IEnumString', 'ISpPhoneConverter', 'SAFTDefault',
    'DISPID_SRCEFalseRecognition', 'DISPID_SpeechPhraseProperties',
    'SPINTERFERENCE_TOOLOUD', 'DISPID_SPRsCount',
    'SAFT32kHz16BitMono', 'DISPID_SpeechRecoResult', 'SITooSlow',
    'DISPID_SLPPartOfSpeech', 'SRAORetainAudio',
    'SPWORDPRONOUNCEABLE', 'SPRECORESULTTIMES', 'SSSPTRelativeToEnd',
    'SPPS_Verb', 'DISPID_SRRecognizer', 'SpCompressedLexicon',
    'SRTSMLTimeout', 'DISPID_SRCState', 'DISPID_SLAddPronunciation',
    'SECFNoSpecialChars', 'SpeechSpecialTransitionType',
    'SpeechLoadOption', 'ISpResourceManager',
    'DISPID_SGRSAddSpecialTransition', 'DISPID_SPERequiredConfidence',
    'SPVPRI_OVER', 'SVP_15', 'SPSHT_NotOverriden', 'SPSMF_UPS',
    'SRAExport', 'Speech_Default_Weight', 'DISPID_SPRules_NewEnum',
    'SP_VISEME_21', 'SPCS_DISABLED', 'DISPIDSPTSI_ActiveLength',
    'SpeechVisemeFeature', 'eLEXTYPE_RESERVED8', 'DISPID_SLWsCount',
    'eLEXTYPE_USER_SHORTCUT', 'DISPID_SpeechObjectToken',
    'SAFTGSM610_11kHzMono', 'SVPAlert', 'SVEBookmark',
    'eLEXTYPE_PRIVATE17', 'SpCustomStream', 'DISPID_SpeechDataKey',
    'DISPID_SAStatus', 'SECFIgnoreCase',
    'ISpeechLexiconPronunciation', 'Speech_StreamPos_Asap',
    'SpeechRecoContextState', 'Speech_Max_Word_Length',
    'DISPID_SGRSTType', 'SVP_5', 'SpUnCompressedLexicon',
    'SpeechAudioVolume', 'SpLexicon', 'SPINTERFERENCE_TOOFAST',
    'DISPID_SRRDiscardResultInfo', 'SpeechDiscardType',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002',
    'SpeechPropertyComplexResponseSpeed', 'eLEXTYPE_PRIVATE14',
    'SGLexicalNoSpecialChars', 'eWORDTYPE_ADDED',
    'DISPID_SREmulateRecognition', 'SPRULESTATE',
    'SpSharedRecognizer', 'SREAudioLevel',
    'DISPID_SRGSetWordSequenceData', 'DISPID_SpeechVoice', 'SVP_13',
    'SPEI_RECO_STATE_CHANGE', 'ISpObjectTokenCategory',
    'SAFTNoAssignedFormat', 'SAFT48kHz8BitStereo',
    'DISPID_SRCERecognizerStateChange', 'UINT_PTR',
    'DISPID_SRCEInterference', 'ISpeechObjectToken',
    'SPXMLRESULTOPTIONS', 'ISpeechXMLRecoResult', 'SDTAudio',
    'ISpeechWaveFormatEx', 'eLEXTYPE_PRIVATE5',
    'DISPID_SpeechPhoneConverter', 'SVP_1', 'SpeechRunState',
    'SpeechCategoryAppLexicons', 'SPINTERFERENCE_NOSIGNAL',
    'SPSMF_SRGS_SAPIPROPERTIES', 'SVP_8', 'DISPID_SVVoice',
    'SAFTCCITT_uLaw_44kHzMono', 'DISPID_SMSSetData',
    'SPRECOCONTEXTSTATUS', 'SAFTCCITT_ALaw_8kHzStereo',
    'DISPID_SpeechBaseStream', 'SVEAllEvents',
    'SAFTCCITT_uLaw_22kHzStereo', 'DISPID_SAEventHandle',
    'SpSharedRecoContext', 'SpeechFormatType', 'SPRST_NUM_STATES',
    'ISpRecognizer', 'SINone', 'SpNullPhoneConverter', 'SPSLMA',
    'SPEI_REQUEST_UI', 'DISPID_SPPs_NewEnum',
    'DISPID_SLRemovePronunciationByPhoneIds', 'eLEXTYPE_PRIVATE2',
    'DISPID_SOTsCount', 'SAFTExtendedAudioFormat',
    'SpeechAudioFormatType', 'DISPID_SRGetPropertyString',
    'DISPID_SOTGetAttribute', 'ISpeechRecoResult', 'SPVISEMES',
    'SPRS_INACTIVE', 'DISPID_SRCEHypothesis', 'SGDSActive',
    'SpPhoneticAlphabetConverter', 'DISPID_SADefaultFormat',
    'SP_VISEME_9', 'STSF_CommonAppData', 'DISPID_SpeechRecoResult2',
    'SpeechTokenValueCLSID', 'SP_VISEME_1', 'SPINTERFERENCE',
    'ISpeechGrammarRuleState', 'SPBINARYGRAMMAR', 'SASPause',
    'ISpeechLexiconWord', 'SPFM_NUM_MODES',
    'DISPID_SASCurrentDevicePosition', 'DISPID_SRCSetAdaptationData',
    'SpeechPropertyAdaptationOn', 'SPWT_DISPLAY',
    'SpeechGrammarTagWildcard', 'SPRECOGNIZERSTATUS',
    '__MIDL_IWinTypes_0009', 'SpeechBookmarkOptions',
    'SpeechWordPronounceable', 'ISpeechPhraseRule', 'WAVEFORMATEX',
    'SPGRAMMARSTATE', 'ISpeechAudioBufferInfo',
    'SSSPTRelativeToCurrentPosition', 'SAFT12kHz16BitStereo',
    'DISPID_SPEs_NewEnum', 'SpeechDictationTopicSpelling',
    'SREFalseRecognition', 'SDTRule', 'SPDKL_CurrentUser',
    'DISPID_SWFESamplesPerSec', 'SPVPRIORITY',
    'DISPID_SpeechWaveFormatEx', 'ISpeechBaseStream',
    'ISpeechLexiconPronunciations', 'DISPID_SAVolume',
    'DISPID_SOTIsUISupported', 'SVPOver', 'SAFTCCITT_uLaw_8kHzMono',
    'SVEAudioLevel', 'SAFTCCITT_ALaw_11kHzStereo',
    'DISPID_SCSBaseStream', 'SPINTERFERENCE_NOISE',
    'SpeechRecognitionType', 'SPEI_MAX_SR', 'DISPID_SRCERecognition',
    'SPWT_LEXICAL_NO_SPECIAL_CHARS', 'DISPID_SPRNumberOfElements',
    'DISPID_SPIRule', 'DISPID_SLWsItem', 'DISPID_SRRSetTextFeedback',
    'SpeechEmulationCompareFlags', 'ISpeechMMSysAudio',
    'DISPID_SPPValue', 'ISpeechRecognizerStatus', 'SRAONone',
    'SpeechRegistryUserRoot', 'ISpMMSysAudio', 'DISPID_SMSAMMHandle',
    'SAFTCCITT_ALaw_44kHzStereo', 'ISpXMLRecoResult',
    'ISpObjectToken', 'SPAR_Low', 'SPEI_ACTIVE_CATEGORY_CHANGED',
    'SpeechAllElements', 'SpeechCategoryAudioOut',
    'SPEI_PROPERTY_STRING_CHANGE', 'DISPID_SLWWord',
    'ISpeechRecoResultDispatch',
    'DISPID_SLAddPronunciationByPhoneIds', 'SRAImport',
    'SPTEXTSELECTIONINFO', 'SPEI_SR_PRIVATE',
    'DISPID_SVSpeakCompleteEvent', 'DISPIDSPTSI_SelectionLength',
    'SpeechCategoryVoices', 'DISPID_SGRsAdd', 'SPSInterjection',
    'DISPID_SPIEnginePrivateData', 'DISPID_SVSInputSentencePosition',
    'SECHighConfidence', 'SPEI_RESERVED5', '_SPAUDIOSTATE',
    'eLEXTYPE_RESERVED7', 'ISpeechGrammarRuleStateTransition',
    'SPGS_ENABLED', 'DISPID_SDKSetLongValue', 'SPCT_SUB_COMMAND',
    'SPPS_Noun', 'SGRSTTWildcard', 'SAFT12kHz16BitMono',
    'DISPID_SLWLangId', 'SRTReSent', 'SWPUnknownWordUnpronounceable',
    'ISpeechLexiconWords', 'SAFTCCITT_ALaw_22kHzMono',
    'ISpeechPhraseReplacements', 'SPAUDIOSTATE', 'ISpeechVoice',
    'DISPIDSPRG', 'DISPID_SRRTLength', 'DISPID_SWFEChannels',
    'SPEI_ADAPTATION', 'DISPID_SVSInputWordPosition',
    'SPEI_HYPOTHESIS', 'ISpAudio', 'DISPID_SOTMatchesAttributes',
    'DISPID_SPIGetText', 'SREPropertyStringChange', 'SPAO_NONE',
    'SP_VISEME_14', 'SpMMAudioEnum', 'SPAS_STOP',
    'DISPID_SPPFirstElement', 'DISPID_SRRRecoContext',
    'DISPID_SRGCmdLoadFromResource', 'SAFT8kHz16BitMono',
    'DISPID_SVAlertBoundary', 'DISPID_SLWType', 'SPCT_SUB_DICTATION',
    'DISPID_SPEAudioSizeBytes', 'SVPNormal', 'SDTProperty',
    'DISPID_SVSLastResult', 'SPAS_PAUSE', 'SSTTTextBuffer',
    'SAFTADPCM_22kHzStereo', 'DISPID_SGRSTRule', 'SRCS_Enabled',
    'DISPID_SRSSupportedLanguages', 'DISPID_SDKGetBinaryValue',
    'SAFTCCITT_uLaw_44kHzStereo', 'SPWP_KNOWN_WORD_PRONOUNCEABLE',
    'SPPARTOFSPEECH', 'SAFTCCITT_uLaw_22kHzMono', 'SPBO_AHEAD',
    'DISPID_SRGCmdSetRuleState', 'DISPID_SpeechAudioBufferInfo',
    'SAFT48kHz16BitMono', 'DISPID_SPEAudioSizeTime',
    'SVSFPurgeBeforeSpeak', 'DISPID_SGRClear', 'DISPID_SVAudioOutput',
    'DISPID_SVResume', 'SITooQuiet', 'SREInterference',
    'SREAllEvents', 'DISPID_SRCBookmark', 'SPSEMANTICERRORINFO',
    'DISPID_SGRSAddRuleTransition',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet', 'IStream',
    'ISpShortcut', 'DISPID_SASetState', 'SPFM_CREATE',
    'eLEXTYPE_USER', 'SPAO_RETAIN_AUDIO', 'DISPID_SPRuleParent',
    'DISPID_SVSRunningState', 'DISPID_SpeechRecognizer',
    'ISpeechFileStream', 'SVSFlagsAsync', 'DISPID_SVEStreamStart',
    'ISpeechRecoResultTimes', 'SP_VISEME_7', 'SPCATEGORYTYPE',
    'ISpVoice', 'SpeechRecognizerState', 'ISpRecognizer3',
    'SpeechGrammarTagDictation', 'SPEI_RESERVED1', 'SRSActive',
    'SPFILEMODE', 'SPEI_RESERVED6', 'SPSVerb', 'SSTTDictation',
    'ISpRecognizer2', 'SPPHRASEREPLACEMENT', 'SLOStatic',
    'DISPID_SGRSTransitions', 'SPWORDTYPE',
    'DISPID_SPERetainedStreamOffset', 'SpPhraseInfoBuilder',
    'SVSFDefault', 'DISPID_SPRulesItem',
    'DISPID_SRCCreateResultFromMemory', 'SDA_Consume_Leading_Spaces',
    'SECFIgnoreWidth', 'SpeechAudioState', 'Library',
    'DISPID_SRSetPropertyString', 'DISPID_SVESentenceBoundary',
    'SGSDisabled', 'SAFT24kHz16BitStereo', 'DISPID_SpeechVoiceStatus',
    'SVP_10', 'DISPID_SLPs_NewEnum', 'DISPID_SPEActualConfidence',
    'DISPID_SABIMinNotification', 'SSFMOpenReadWrite',
    'SECNormalConfidence', 'SLTUser', 'ISpNotifySource',
    'DISPID_SPCLangId', 'SpeechStreamSeekPositionType',
    'DISPID_SOTCGetDataKey', 'SPEI_PHRASE_START', 'SPWF_INPUT',
    'SPAR_Unknown', 'SPVPRI_NORMAL', 'eLEXTYPE_VENDORLEXICON',
    'ISpeechObjectTokenCategory', 'SVP_0', 'DISPID_SVSLastBookmark',
    'ISpeechObjectTokens', 'ISpSerializeState', 'SRSActiveAlways',
    'STCLocalServer', 'DISPID_SRGDictationUnload', 'SVF_None',
    'ISpPhraseAlt', 'DISPID_SABIBufferSize', 'DISPID_SFSOpen',
    'tagSTATSTG', 'SpeechAudioFormatGUIDWave', 'SVP_3', 'SRSEDone',
    'SPRS_ACTIVE_USER_DELIMITED', 'DISPID_SRCRequestedUIType',
    'DISPIDSPTSI_ActiveOffset', 'DISPID_SRCAudioInInterferenceStatus',
    'SPPS_SuppressWord', 'DISPID_SOTCDefault', 'SVSFNLPMask',
    'SPCT_SLEEP', 'SGRSTTDictation', 'SPEI_PHONEME',
    'DISPID_SPISaveToMemory', 'DISPID_SVEAudioLevel',
    'ISpNotifyTranslator', 'SP_VISEME_20', 'ISpeechRecoGrammar',
    'SECFDefault', 'SP_VISEME_17', 'SVSFIsXML', 'DISPID_SGRSTsItem',
    'DISPID_SRRAudio', 'DISPID_SRState', 'DISPID_SDKSetBinaryValue',
    'SWPKnownWordPronounceable', 'eLEXTYPE_PRIVATE8', 'SP_VISEME_18',
    'SPXRO_SML', 'SRSEIsSpeaking', 'DISPID_SOTGetStorageFileName',
    'SVSFVoiceMask', 'SPSHORTCUTTYPE', 'SECFIgnoreKanaType',
    'SDTReplacement', 'DISPID_SPAsCount', 'DISPID_SpeechMMSysAudio',
    'SAFT12kHz8BitMono', 'SpeechRetainedAudioOptions',
    'DISPID_SPAPhraseInfo', 'SAFT8kHz8BitMono', 'SP_VISEME_11',
    'SPPS_RESERVED1', 'DISPID_SLWPronunciations',
    'DISPID_SMSADeviceId', 'SDTDisplayText',
    'DISPID_SWFEAvgBytesPerSec', 'SVEVoiceChange',
    'SPRST_INACTIVE_WITH_PURGE', 'SVP_19', 'DISPID_SDKGetlongValue',
    'SAFT22kHz16BitMono', 'DISPID_SVEWord', 'SPPS_Unknown',
    'SpeechTokenIdUserLexicon', 'DISPID_SOTs_NewEnum', 'SDTAll',
    'SAFTADPCM_22kHzMono', 'DISPID_SRRGetXMLErrorInfo',
    'SPPS_Noncontent', 'SPDKL_CurrentConfig', 'ISpeechResourceLoader',
    'DISPID_SPIElements', 'SVSFIsFilename', 'DISPID_SVWaitUntilDone',
    'DISPID_SAFGetWaveFormatEx', 'SPEI_UNDEFINED',
    'SPEI_TTS_AUDIO_LEVEL', 'DISPID_SpeechPhraseReplacement',
    'SpeechMicTraining', 'DISPID_SGRSTText', 'DISPID_SGRsFindRule',
    'DISPID_SVAudioOutputStream', 'DISPID_SGRSTs_NewEnum',
    'SpObjectToken', 'ISpDataKey', 'DISPID_SBSFormat',
    'DISPID_SLGetPronunciations', 'DISPID_SpeechLexiconPronunciation',
    'DISPID_SPRuleConfidence', 'DISPID_SRRPhraseInfo',
    'SDKLCurrentUser', 'DISPID_SVSLastBookmarkId',
    'SpeechEngineConfidence', 'SDKLLocalMachine', 'STCRemoteServer',
    'DISPID_SRGReset', 'DISPID_SRCESoundEnd',
    'SAFTTrueSpeech_8kHz1BitMono', 'DISPID_SPPChildren',
    'SPFM_CREATE_ALWAYS', 'SPSNoun', 'SAFTNonStandardFormat',
    'SpeechAudioFormatGUIDText', 'SPEI_VISEME', 'SECFEmulateResult',
    'DISPID_SBSWrite', 'DISPID_SPAStartElementInResult',
    'DISPID_SOTSetId', 'ISpProperties', 'DISPID_SPEPronunciation',
    'SGLexical', 'Speech_Max_Pron_Length', 'tagSPPROPERTYINFO',
    'SPEI_SR_RETAINEDAUDIO', 'DISPID_SPAsItem',
    'DISPID_SpeechRecoContext', 'DISPID_SRCEPhraseStart',
    'DISPID_SGRsCount', 'DISPID_SRDisplayUI',
    'ISpeechPhraseProperties', 'SPEI_TTS_PRIVATE',
    'DISPID_SLGenerationId', 'DISPID_SVSLastStreamNumberQueued',
    'SPAUDIOBUFFERINFO', 'DISPID_SWFEBlockAlign',
    'DISPID_SVSPhonemeId', 'DISPID_SpeechMemoryStream',
    'SDA_Two_Trailing_Spaces', 'SVP_2', 'SVP_9',
    'SpeechVoiceSkipTypeSentence', 'DISPID_SPRuleChildren',
    'DISPID_SVSpeakStream', 'SAFT32kHz8BitMono',
    'ISpStreamFormatConverter', 'SpInProcRecoContext',
    'SPPS_RESERVED3', 'SpStream',
    'SpeechPropertyHighConfidenceThreshold', 'SPRECOSTATE',
    'SPXRO_Alternates_SML', 'SAFT16kHz16BitMono',
    'SpeechRegistryLocalMachineRoot', 'SPSHT_Unknown',
    'eLEXTYPE_PRIVATE13', 'SPWT_LEXICAL', 'DISPID_SGRSTPropertyId',
    'IEnumSpObjectTokens', 'DISPIDSPTSI', 'SpeechDataKeyLocation',
    'DISPID_SOTsItem', 'SPWF_SRENGINE', 'DISPID_SVPause',
    'ISpeechAudio', 'DISPID_SRRSpeakAudio',
    'DISPID_SVSInputWordLength', 'ISpeechPhraseAlternates',
    'SpeechLexiconType', 'DISPID_SLWs_NewEnum', 'SPEI_SOUND_START',
    'SPEI_START_SR_STREAM', 'SPWORDPRONUNCIATIONLIST',
    'ISpeechCustomStream', 'ISpeechPhraseReplacement',
    'DISPID_SPERetainedSizeBytes', 'DISPID_SPPEngineConfidence',
    'SP_VISEME_0', 'SVSFIsNotXML', 'SPPS_RESERVED4', 'DISPID_SRGId',
    'ISpRecoContext', 'SVP_7', 'DISPID_SGRSTPropertyName',
    'SAFTADPCM_11kHzStereo', 'DISPID_SPRulesCount',
    'SPWORDPRONUNCIATION', 'SAFTADPCM_11kHzMono',
    'DISPID_SpeechVoiceEvent', 'DISPID_SPPParent', 'SPAR_Medium',
    'DISPID_SRGCommit', 'SREBookmark', 'SPPS_RESERVED2',
    'DISPID_SpeechObjectTokens', 'DISPID_SVRate', 'DISPID_SPPsCount',
    'eLEXTYPE_PRIVATE18', 'SPEI_VOICE_CHANGE', 'SVP_16',
    'DISPID_SRProfile', 'SpShortcut', 'SPSHT_EMAIL',
    'SAFT44kHz16BitMono', 'DISPID_SpeechPhraseElement',
    'DISPID_SOTCEnumerateTokens', 'tagSPTEXTSELECTIONINFO',
    'DISPID_SDKSetStringValue', 'SFTSREngine', 'DISPID_SABufferInfo',
    'DISPID_SPRuleId', 'SAFTCCITT_ALaw_8kHzMono',
    'DISPID_SpeechFileStream', 'DISPID_SVSCurrentStreamNumber',
    'DISPID_SRGetRecognizers', 'SAFT16kHz16BitStereo', 'SRESoundEnd',
    'SDTAlternates', 'SRERequestUI', 'SPINTERFERENCE_TOOQUIET',
    'SLTApp', 'SP_VISEME_10', 'DISPID_SpeechPhraseInfo',
    'eLEXTYPE_PRIVATE12', 'SpeechTokenKeyAttributes',
    'SAFTADPCM_44kHzMono', 'SITooLoud', 'SPEI_MIN_TTS',
    'SREStreamEnd', 'ISpeechVoiceStatus', 'SpeechVoiceSpeakFlags',
    'SpWaveFormatEx', 'DISPID_SPIStartTime', 'DISPID_SMSALineId',
    'DISPID_SRCRecognizer', 'SP_VISEME_8', 'DISPID_SVStatus',
    'eLEXTYPE_PRIVATE4', 'DISPID_SOTCreateInstance',
    'DISPID_SRCEAudioLevel', 'DISPID_SASNonBlockingIO',
    'ISpRecoContext2', 'DISPID_SABIEventBias', 'SAFT16kHz8BitStereo',
    'DISPID_SVSkip', 'SPWT_PRONUNCIATION', 'DISPID_SOTDisplayUI',
    'DISPID_SRAudioInputStream', 'SPBO_NONE', 'SpeechInterference',
    'SAFTCCITT_uLaw_11kHzMono', 'DISPID_SRRAudioFormat',
    'SPRST_ACTIVE_ALWAYS', 'DISPID_SLPLangId', 'SPVPRI_ALERT',
    'SpeechCategoryAudioIn', 'SRADefaultToActive',
    'DISPID_SOTCategory', 'DISPID_SVGetProfiles', 'DISPID_SVEViseme',
    'SPEI_START_INPUT_STREAM',
    '__MIDL___MIDL_itf_sapi_0000_0020_0001',
    'DISPID_SpeechRecognizerStatus', 'DISPID_SFSClose',
    'DISPID_SPELexicalForm', 'DISPID_SpeechGrammarRule',
    'SPSMF_SAPI_PROPERTIES', 'ISpeechGrammarRule',
    'STSF_LocalAppData', 'ISpStreamFormat', 'STCInprocServer',
    'DISPID_SPCIdToPhone', 'SAFT32kHz16BitStereo',
    'DISPID_SWFEExtraData', 'eLEXTYPE_RESERVED6',
    'DISPID_SOTRemoveStorageFileName', 'DISPID_SLGetGenerationChange',
    'eLEXTYPE_PRIVATE6', 'SPBO_PAUSE', 'SpStreamFormatConverter',
    'SPPROPERTYINFO', 'DISPID_SPPNumberOfElements',
    'SpeechEngineProperties', 'SP_VISEME_13', 'SPEI_SR_AUDIO_LEVEL',
    'DISPID_SGRSTNextState', 'SAFTADPCM_44kHzStereo',
    'SPBO_TIME_UNITS', 'ISpRecoCategory', 'ISpeechPhraseElement',
    'SPEI_RECO_OTHER_CONTEXT', 'SAFTGSM610_8kHzMono',
    'SpeechStreamFileMode', 'DISPID_SVEVoiceChange',
    'DISPID_SPANumberOfElementsInResult', 'DISPID_SGRInitialState',
    'DISPID_SVGetAudioOutputs', 'DISPID_SRIsUISupported',
    'SPCT_DICTATION', 'SpeechCategoryPhoneConverters', 'SSTTWildcard',
    'SVESentenceBoundary', 'SPPHRASEPROPERTY', 'SBOPause',
    'DISPID_SPPsItem', 'SPEI_WORD_BOUNDARY',
    'DISPID_SpeechObjectTokenCategory', 'SAFT12kHz8BitStereo',
    'DISPID_SpeechPhraseRules', 'ISpeechRecoResult2', 'SPAUDIOSTATUS',
    'DISPID_SGRAddResource', 'ISpStream', 'eLEXTYPE_APP',
    'SSFMOpenForRead', 'SpFileStream', 'DISPID_SRCEStartStream',
    'SAFT24kHz8BitMono', 'DISPID_SASState', 'DISPID_SPCPhoneToId',
    'SpMemoryStream', 'DISPID_SOTRemove', 'DISPID_SOTCId',
    'SPLO_DYNAMIC', 'ISpGrammarBuilder', 'SGRSTTRule',
    'SPINTERFERENCE_LATENCY_WARNING', 'ISpeechDataKey',
    'SRTAutopause', 'DISPID_SRGSetTextSelection',
    'DISPID_SpeechPhraseRule', 'SPRS_ACTIVE', 'ISpeechMemoryStream',
    'DISPID_SpeechLexiconProns',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'DISPID_SPIReplacements',
    'SSSPTRelativeToStart', 'SSFMCreateForWrite',
    'SpeechGrammarWordType', 'DISPID_SRRTStreamTime',
    'SAFT32kHz8BitStereo', 'DISPID_SRCRetainedAudio', 'SASClosed',
    'DISPID_SRGCmdLoadFromFile', 'SAFTGSM610_44kHzMono', 'SGRSTTWord',
    'DISPID_SPRuleEngineConfidence', 'eLEXTYPE_PRIVATE1',
    'SPAS_CLOSED', 'SDA_One_Trailing_Space', 'SPEVENTENUM',
    'SpeechVoiceEvents', 'DISPID_SMSGetData', 'SPDKL_DefaultLocation',
    'SpeechRecoProfileProperties', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'SAFTADPCM_8kHzStereo', 'DISPID_SOTGetDescription',
    'SPPHRASERULE', 'SVSFParseSapi', 'SPRST_ACTIVE',
    'DISPID_SRCPause', 'ISpeechTextSelectionInformation',
    'SVSFParseAutodetect', 'DISPID_SVSyncronousSpeakTimeout',
    'ISpeechPhraseProperty', 'SPFM_OPEN_READWRITE',
    'DISPID_SLGetWords', 'eLEXTYPE_PRIVATE11',
    'DISPID_SRCEPropertyStringChange', 'DISPID_SGRSAddWordTransition',
    'SpInprocRecognizer', 'eLEXTYPE_LETTERTOSOUND', 'SPSHT_OTHER',
    'SpMMAudioIn', 'DISPID_SRSCurrentStreamPosition',
    'eLEXTYPE_PRIVATE19', 'DISPID_SPEAudioStreamOffset',
    'SRESoundStart', 'SAFT24kHz8BitStereo',
    'SpeechPropertyNormalConfidenceThreshold', 'SPEI_END_SR_STREAM',
    'ISpeechLexicon', 'SPSERIALIZEDPHRASE', 'SpVoice',
    'DISPID_SDKDeleteKey', 'eLEXTYPE_RESERVED9', 'SREStreamStart',
    'DISPID_SpeechRecoResultTimes', 'DISPID_SPARecoResult',
    'DISPID_SGRSTsCount', 'SGDSActiveWithAutoPause', 'SASStop',
    'SVSFUnusedFlags', 'SREPrivate', 'DISPID_SBSRead',
    'SPEVENTSOURCEINFO', 'SPLOADOPTIONS', 'DISPID_SRStatus',
    'SpPhoneConverter', 'SPAUDIOOPTIONS', 'SRARoot',
    'DISPID_SpeechPhraseElements', 'eLEXTYPE_PRIVATE7',
    'SAFT44kHz8BitStereo', 'DISPID_SPEAudioTimeOffset',
    'SRSInactiveWithPurge', 'SAFTCCITT_ALaw_11kHzMono',
    'DISPID_SGRId', 'ISpPhoneticAlphabetConverter', 'SINoSignal',
    'DISPID_SAFGuid', 'SAFT8kHz16BitStereo', 'SpeechWordType',
    'SAFT24kHz16BitMono', 'SRADynamic', 'SPCS_ENABLED',
    'SPEI_RESERVED3', 'DISPID_SRGetPropertyNumber',
    'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN',
    'DISPID_SRCEPropertyNumberChange', 'DISPID_SpeechAudioFormat',
    'DISPID_SpeechLexiconWords', 'DISPID_SRCCmdMaxAlternates',
    'DISPID_SWFEFormatTag', 'SPINTERFERENCE_NONE',
    'DISPID_SpeechPhraseBuilder', 'SGSExclusive', 'DISPID_SOTId',
    'SpeechDisplayAttributes', 'SPEI_INTERFERENCE',
    'DISPID_SPRuleFirstElement', 'DISPID_SGRSTPropertyValue',
    'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'ISpObjectWithToken', 'STCAll',
    'eWORDTYPE_DELETED', 'SPADAPTATIONRELEVANCE',
    'SpeechPropertyLowConfidenceThreshold', 'DISPID_SLPSymbolic',
    'DISPID_SPIAudioStreamPosition', 'DISPID_SpeechAudio',
    'SPSERIALIZEDRESULT', 'DISPID_SRCEventInterests',
    'SpeechVoicePriority', 'SGRSTTEpsilon', 'DISPID_SPPConfidence',
    'DISPID_SPILanguageId', 'SP_VISEME_16', 'SAFT48kHz16BitStereo',
    'SPSTREAMFORMATTYPE', 'DISPID_SOTDataKey',
    'DISPID_SVGetAudioInputs', 'SpeechPropertyResourceUsage',
    'DISPID_SpeechPhraseAlternate', 'DISPID_SPRText',
    'SAFTCCITT_uLaw_11kHzStereo', 'DISPID_SRCESoundStart',
    'SAFTCCITT_ALaw_44kHzMono', 'SpeechAudioProperties',
    'SPGRAMMARWORDTYPE', 'DISPID_SRGCmdLoadFromProprietaryGrammar',
    'SP_VISEME_4', 'ISpPhrase', 'SAFT44kHz16BitStereo',
    'SAFT16kHz8BitMono', 'DISPID_SVSVisemeId', 'SPPS_LMA',
    'SPFM_OPEN_READONLY', 'DISPID_SGRsItem', 'DISPID_SGRSRule',
    'SPSUnknown', '_ISpeechVoiceEvents', 'DISPID_SGRAttributes',
    'SRATopLevel', 'DISPID_SABufferNotifySize', 'SpeechVisemeType',
    'DISPID_SPEDisplayText', 'SWPUnknownWordPronounceable',
    'SWTDeleted', 'DISPID_SpeechAudioStatus',
    'SGDSActiveUserDelimited', 'DISPID_SRGCmdLoadFromObject',
    'SPEI_END_INPUT_STREAM', 'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE',
    'SpeechTokenKeyFiles', 'SpeechCategoryRecognizers',
    'eLEXTYPE_RESERVED10', 'SPPHRASEELEMENT', 'SSFMCreate',
    'DISPID_SpeechGrammarRuleStateTransition', 'STSF_AppData',
    'DISPID_SPIAudioSizeBytes', 'SPLO_STATIC',
    'DISPID_SRCEAdaptation', 'SPEI_SOUND_END', 'SGDisplay',
    'SECLowConfidence', 'SPRST_INACTIVE', 'DISPID_SVEventInterests',
    'ISpeechAudioFormat', 'ISpeechAudioStatus',
    'DISPID_SpeechLexicon', 'SAFT48kHz8BitMono',
    'DISPID_SVSInputSentenceLength', 'DISPID_SRRSaveToMemory',
    'SDTLexicalForm', '_ISpeechRecoContextEvents', 'SVP_20', 'SVP_11',
    'SpeechGrammarState', 'SPPS_Interjection', 'SPPHRASE',
    'SAFT22kHz16BitStereo', 'SREPhraseStart',
    'ISpeechPhraseAlternate', 'LONG_PTR', 'ISpeechPhraseElements',
    'SPSHORTCUTPAIR', 'SpeechAddRemoveWord', 'SpeechTokenContext',
    'SVF_Stressed', 'Speech_StreamPos_RealTime', 'ISpeechRecoContext',
    'ISpPhoneticAlphabetSelection', 'eLEXTYPE_MORPHOLOGY',
    'DISPID_SpeechLexiconWord', 'DISPID_SRRGetXMLResult',
    'DISPID_SGRName', 'DISPID_SWFEBitsPerSample', 'SPLEXICONTYPE',
    'DISPID_SPIRetainedSizeBytes', 'DISPID_SpeechRecoContextEvents',
    'DISPID_SpeechPhraseProperty', 'SAFTGSM610_22kHzMono',
    'DISPID_SBSSeek', 'SAFT11kHz16BitMono', 'SRERecoOtherContext',
    'SPWORD', 'DISPID_SDKDeleteValue', 'DISPID_SLPsItem',
    'DISPID_SRCEEnginePrivate', 'SpNotifyTranslator', 'SGSEnabled',
    'SGDSInactive', 'SVEViseme', 'DISPID_SLRemovePronunciation',
    'SpeechRuleAttributes', 'DISPID_SPEDisplayAttributes',
    'SAFT11kHz8BitStereo', 'DISPID_SPPId',
    'DISPID_SRSNumberOfActiveRules', 'DISPID_SPRuleNumberOfElements',
    'SLODynamic', 'SP_VISEME_5', 'SRTExtendableParse', 'SVP_12',
    'DISPID_SDKEnumKeys', 'DISPID_SVPriority',
    'SAFTCCITT_uLaw_8kHzStereo', 'DISPID_SRGState',
    'DISPID_SVEPhoneme', 'SpeechRecoEvents', 'SP_VISEME_3',
    'SPEI_PROPERTY_NUM_CHANGE', 'SpeechGrammarTagUnlimitedDictation',
    'SP_VISEME_6', 'DISPID_SRRTimes', 'ISpRecoGrammar2',
    'SREPropertyNumChange', 'SDA_No_Trailing_Space', 'ISpLexicon',
    'ISpEventSource', 'DISPID_SPRs_NewEnum',
    'DISPID_SRSetPropertyNumber', 'SVEPrivate',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'SPEI_FALSE_RECOGNITION'
]

