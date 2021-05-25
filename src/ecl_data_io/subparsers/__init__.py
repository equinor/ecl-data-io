from .columns_parser import ColumnsSubParser
from .one_line_parser import OneLineSubParser
from .simple_data_subparser import SimpleDataSubParser
from .single_keyword_parser import SingleKeywordSubParser
from .skip_parser import SkipSubParser
from .tabdims_parser import (
    TabdimsSubParser,
    get_nmeosr,
    get_nmeoss,
    get_nppvt,
    get_ntalpha,
    get_ntcreg,
    get_ntpvt,
    get_ntsfun,
)

DEFAULT_SUBPARSERS = [
    OneLineSubParser("MESSAGE"),
    ColumnsSubParser(),
    SkipSubParser("SKIP"),
    SkipSubParser("SKIP100"),
    SingleKeywordSubParser("ENDSKIP"),
    SingleKeywordSubParser("SKIP300"),
]

single_keywords = [
    "AIM",
    "AITS",
    "AITSOFF",
    "AJGRADNT",
    "ALKALINE",
    "API",
    "BIGMODEL",
    "BLACKOIL",
    "CART",
    "CIRCLE",
    "CO2STORE",
    "COAL",
    "COMPOFF",
    "DEADOIL",
    "DIAGDISP",
    "DIFFDP",
    "DIFFUSE",
    "DIMPLICIT",
    "DISGAS",
    "DPGRID",
    "DRAINAGE",
    "DSPDEINT",
    "DUALPERM",
    "DUALPORO",
    "DUMPFLUX",
    "E100NOSI",
    "ECHO",
    "ECLMC",
    "END",
    "ACTION",
    "ACTIONG",
    "ACTIONR",
    "ACTIONW",
    "ENDACTIO",
    "BOX",
    "ENDBOX",
    "DYNAMICR",
    "ENDDYN",
    "ENDFIN",
    "ENDINC",
    "EPSCHECK",
]

simple_data_keywords = [
    "ACTCO2S",
    "ACTDIMS",
    "ACTNUM",
    "ACTPARAM",
    "AIMCON",
    "AIMFRAC",
    "AIMPVI",
    "AJGPARAM",
    "ALPHANUD",
    "ALPHANUI",
    "ALPHANUM",
    "APIGROUP",
    "APILIM",
    "AQCOEF",
    "AQUCWFAC",
    "AQUDIMS",
    "AQUTAB",
    "ASPDEPO",
    "ASPFLOC",
    "ASPFLRT",
    "ASPHALTE",
    "ASPKDAM",
    "ASPLCRT",
    "ASPP1P",
    "ASPP2P",
    "ASPREWG",
    "ASPVISO",
    "ASPWETF",
    "AUTOREF",
    "AUTOSAVE",
    "BAKER1",
    "BAKER2",
    "BOUNDARY",
    "BOX",
    "BPARA",
    "BPDIMS",
    "BRINE",
    "BTOBALFA",
    "BTOBALFV",
    "CALTRAC",
    "CALVAL",
    "CATYPE",
    "CBMOPTS",
    "CFLLIMIT",
    "CHANDIMS",
    "CNAMES",
    "COALNUM",
    "COMPS",
    "COMPSOL",
    "COMPVD",
    "COMPVE",
    "COMPVEL",
    "COORD",
    "CPR",
    "CRITPERM",
    "COMPW",
    "CVCRIT",
    "CWTYPE",
    "DATUM",
    "DATUMR",
    "DBGODD3P",
    "DCQDEFN",
    "DEBUG",
    "DEBUG3",
    "DELAYACT",
    "DEPTH",
    "DGRDT",
    "DGRID",
    "DIFFCGAS",
    "DIFFCGO",
    "DIFFCGW",
    "DIFFCOG",
    "DIFFCOIL",
    "DIFFCWG",
    "DIFFMMF",
    "DIFFMR",
    "DIFFMR-",
    "DIFFMTHT",
    "DIFFMTH-",
    "DIFFMX",
    "DIFFMX-",
    "DIFFMY",
    "DIFFMY-",
    "DIFFMZ",
    "DIFFMZ-",
    "DIFFR",
    "DIFFTGAS",
    "DIFFTHT",
    "DIFFTOIL",
    "DIFFX",
    "DIFFY",
    "DIFFZ",
    "DIMENS",
    "DIMPES",
    "DISPDIMS",
    "DNGL",
    "DOMAIN",
    "DOMAINS",
    "DPCDT",
    "DPNUM",
    "DR",
    "DRILPRI",
    "DRSDT",
    "DRV",
    "DRVDT",
    "DSTNUM",
    "DTHETA",
    "DTHETAV",
    "DUMPCUPL",
    "DX",
    "DXV",
    "DY",
    "DYV",
    "DZ",
    "DZV",
    "DYNRDIMS",
    "DZMATRIX",
    "DZMATRX",
    "DZMATRXV",
    "DZNET",
    "EHYSTR",
    "CARFIN",
    "RADFIN",
    "RADFIN4",
    "REFINE",
    "ENDNUM",
    "ENDSCALE",
    "EOSNUM",
    "EPSCOMP",
    "EPSDEBUG",
    "EQLDIMS",
    "EQLDKVCR",
    "EQLDTAB",
    "EQLNUM",
    "EQLOPTS",
]

double_data_keywords = [
    "ADD",
    "ADDREG",
    "ADDZCORN",
    "AJGWELLS",
    "AMALGAM",
    "AQANCONL",
    "AQANNC",
    "AQANTRC",
    "AQSTREAM",
    "AQSTREAW",
    "AQUALIST",
    "AQUANCON",
    "AQUCHGAS",
    "AQUCHWAT",
    "AQUCON",
    "AQUCT",
    "AQUFETP",
    "AQUFLUX",
    "AQUNNC",
    "AQUNUM",
    "ASPPW2D",
    "AUTOCOAR",
    "BRANPROP",
    "CECON",
    "COALNUMR",
    "COARSEN",
    "COLLAPSE",
    "COMPAGH",
    "COMPAGHL",
    "COMPDAT",
    "COMPDATL",
    "COMPDATM",
    "COMPFLSH",
    "COMPIMB",
    "COMPINJK",
    "COMPKRI",
    "COMPKRIL",
    "COMPLMPL",
    "COMPLUMP",
    "COMPMBIL",
    "COMPMOBI",
    "COMPORD",
    "COMPRIV",
    "COMPRP",
    "COMPRPL",
    "COMPSEGL",
    "COMPSEGS",
    "CONDFLTS",
    "CONDFRAC",
    "COPY",
    "COPYBOX",
    "COPYREG",
    "CPIFACT",
    "CPIFACTL",
    "CRNDENS",
    "CSKIN",
    "DATES",
    "DATUMRX",
    "DIFFCBM",
    "EDITNNCR",
    "EPSDBGS",
    "EQLZCORN",
    "EQUALREG",
    "EQUALS",
]

triple_data_keywords = [
    "CECONT",
]


tabdims_keywords = [
    ("ACF", get_nmeosr),
    ("ACFDET", get_nmeosr),
    ("ACFS", get_nmeoss),
    ("ADSALNOD", get_ntsfun),
    ("ADSORP", lambda x: get_ntsfun(x) + 1),
    ("ALKADS", get_ntsfun),
    ("ALKROCK", get_ntsfun),
    ("ALPHA", get_ntalpha),
    ("ALPHAD", get_ntalpha),
    ("ALPHAI", get_ntalpha),
    ("ALPOLADS", get_ntsfun),
    ("ALSURFAD", get_ntsfun),
    ("ALSURFST", get_nppvt),
    ("ASPKROW", get_ntsfun),
    ("BDENSITY", get_ntpvt),
    ("BIC", get_nmeosr),
    ("CTYPE", get_nmeosr),
    ("CTYPES", get_nmeosr),
    ("CGDTYPE", get_nmeosr),
    ("CGVTYPE", get_nmeosr),
    ("COALADS", get_ntcreg),
    ("CODTYPE", get_nmeosr),
    ("COVTYPE", get_nmeosr),
    ("CREF", get_nmeosr),
    ("CREFW", get_nmeosr),
    ("CREFWS", get_nmeoss),
    ("CVTYPE", get_nmeosr),
    ("CVTYPES", get_nmeoss),
    ("DENAQA", get_nmeosr),
    ("DIFFC", get_ntpvt),
    ("DPKRMOD", get_ntsfun),
    ("DREF", get_nmeosr),
    ("DREFS", get_nmeoss),
    ("DREFW", get_nmeosr),
    ("DREFWS", get_nmeoss),
    ("DRSDTR", get_ntpvt),
    ("EHYSTRR", get_ntsfun),
    ("ENKRVC", get_ntsfun),
    ("ENKRVT", get_ntsfun),
    ("ENPCVC", get_ntsfun),
    ("ENPTVC", get_ntsfun),
    ("ENPCVT", get_ntsfun),
    ("ENPTVT", get_ntsfun),
    ("EOS", get_nmeosr),
    ("EOSS", get_nmeoss),
    ("EPSODD3P", get_ntsfun),
    ("ESPNODE", get_ntpvt),
]

COMMON_SUBPARSERS = [
    SimpleDataSubParser("GDORIENT"),
    SimpleDataSubParser("SPECGRID"),
    SimpleDataSubParser("COORD"),
    SimpleDataSubParser("ZCORN"),
    SimpleDataSubParser("ACTNUM"),
    SimpleDataSubParser("DIMENS"),
    SimpleDataSubParser("GRIDOPTS"),
    SingleKeywordSubParser("OIL"),
    SingleKeywordSubParser("WATER"),
    SingleKeywordSubParser("GAS"),
    SingleKeywordSubParser("DISGAS"),
    SingleKeywordSubParser("VAPOIL"),
    SingleKeywordSubParser("NOECHO"),
    SingleKeywordSubParser("ECHO"),
    SingleKeywordSubParser("RUNSPEC"),
    SingleKeywordSubParser("GRID"),
    SingleKeywordSubParser("EDIT"),
    SingleKeywordSubParser("PROPS"),
    SingleKeywordSubParser("REGIONS"),
    SingleKeywordSubParser("SOLUTION"),
    SingleKeywordSubParser("SUMMARY"),
    SingleKeywordSubParser("SCHEDULE"),
    SingleKeywordSubParser("END"),
]
