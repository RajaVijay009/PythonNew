
"""Please find below the code we need to change. Basically we need to change the current query to SAP by adding more tables and
 by including the new data in the file the code generate.
Please let me know if is something you can work on and I’ll give you the detailed specs."""




from ctypes import *

import platform, os

 

def saprpc(urc):

                #-Main------------------------------------------------------------------

                #-Packages--------------------------------------------------------------

 

 

                #-Structures------------------------------------------------------------

                class RFC_ERROR_INFO(Structure):

                                _fields_ = [("code", c_long),

                                                                                ("group", c_long),

                                                                                ("key", c_wchar * 128),

                                                                                ("message", c_wchar * 512),

                                                                                ("abapMsgClass", c_wchar * 21),

                                                                                ("abapMsgType", c_wchar * 2),

                                                                                ("abapMsgNumber", c_wchar * 4),

                                                                                ("abapMsgV1", c_wchar * 51),

                                                                                ("abapMsgV2", c_wchar * 51),

                                                                                ("abapMsgV3", c_wchar * 51),

                                                                                ("abapMsgV4", c_wchar * 51)]

 

                class RFC_CONNECTION_PARAMETER(Structure):

                                _fields_ = [("name", c_wchar_p),

                                                                                ("value", c_wchar_p)]

 

 

                #-Constants-------------------------------------------------------------

 

                #-RFC_RC - RFC return codes---------------------------------------------

                RFC_OK = 0

                RFC_COMMUNICATION_FAILURE = 1

                RFC_LOGON_FAILURE = 2

                RFC_ABAP_RUNTIME_FAILURE = 3

                RFC_ABAP_MESSAGE = 4

                RFC_ABAP_EXCEPTION = 5

                RFC_CLOSED = 6

                RFC_CANCELED = 7

                RFC_TIMEOUT = 8

                RFC_MEMORY_INSUFFICIENT = 9

                RFC_VERSION_MISMATCH = 10

                RFC_INVALID_PROTOCOL = 11

                RFC_SERIALIZATION_FAILURE = 12

                RFC_INVALID_HANDLE = 13

                RFC_RETRY = 14

                RFC_EXTERNAL_FAILURE = 15

                RFC_EXECUTED = 16

                RFC_NOT_FOUND = 17

                RFC_NOT_SUPPORTED = 18

                RFC_ILLEGAL_STATE = 19

                RFC_INVALID_PARAMETER = 20

                RFC_CODEPAGE_CONVERSION_FAILURE = 21

                RFC_CONVERSION_FAILURE = 22

                RFC_BUFFER_TOO_SMALL = 23

                RFC_TABLE_MOVE_BOF = 24

                RFC_TABLE_MOVE_EOF = 25

                RFC_START_SAPGUI_FAILURE = 26

                RFC_ABAP_CLASS_EXCEPTION = 27

                RFC_UNKNOWN_ERROR = 28

                RFC_AUTHORIZATION_FAILURE = 29

 

                #-RFCTYPE - RFC data types----------------------------------------------

                RFCTYPE_CHAR = 0

                RFCTYPE_DATE = 1

                RFCTYPE_BCD = 2

                RFCTYPE_TIME = 3

                RFCTYPE_BYTE = 4

                RFCTYPE_TABLE = 5

                RFCTYPE_NUM = 6

                RFCTYPE_FLOAT = 7

                RFCTYPE_INT = 8

                RFCTYPE_INT2 = 9

                RFCTYPE_INT1 = 10

                RFCTYPE_NULL = 14

                RFCTYPE_ABAPOBJECT = 16

                RFCTYPE_STRUCTURE = 17

                RFCTYPE_DECF16 = 23

                RFCTYPE_DECF34 = 24

                RFCTYPE_XMLDATA = 28

                RFCTYPE_STRING = 29

                RFCTYPE_XSTRING = 30

                RFCTYPE_BOX = 31

                RFCTYPE_GENERIC_BOX = 32

 

                #-RFC_UNIT_STATE - Processing status of a background unit---------------

                RFC_UNIT_NOT_FOUND = 0

                RFC_UNIT_IN_PROCESS = 1

                RFC_UNIT_COMMITTED = 2

                RFC_UNIT_ROLLED_BACK = 3

                RFC_UNIT_CONFIRMED = 4

 

                #-RFC_CALL_TYPE - Type of an incoming function call---------------------

                RFC_SYNCHRONOUS = 0

                RFC_TRANSACTIONAL = 1

                RFC_QUEUED = 2

                RFC_BACKGROUND_UNIT = 3

 

                #-RFC_DIRECTION - Direction of a function module parameter--------------

                RFC_IMPORT = 1

                RFC_EXPORT = 2

                RFC_CHANGING = RFC_IMPORT + RFC_EXPORT

                RFC_TABLES = 4 + RFC_CHANGING

 

                #-RFC_CLASS_ATTRIBUTE_TYPE - Type of an ABAP object attribute-----------

                RFC_CLASS_ATTRIBUTE_INSTANCE = 0

                RFC_CLASS_ATTRIBUTE_CLASS = 1

                RFC_CLASS_ATTRIBUTE_CONSTANT = 2

 

                #-RFC_METADATA_OBJ_TYPE - Ingroup repository----------------------------

                RFC_METADATA_FUNCTION = 0

                RFC_METADATA_TYPE = 1

                RFC_METADATA_CLASS = 2

 

 

                #-Variables-------------------------------------------------------------

                ErrInf = RFC_ERROR_INFO; RfcErrInf = ErrInf()

                ConnParams = RFC_CONNECTION_PARAMETER * 5; RfcConnParams = ConnParams()

                SConParams = RFC_CONNECTION_PARAMETER * 3; RfcSConParams = SConParams()

 

 

                #-Library---------------------------------------------------------------

                if str(platform.architecture()[0]) == "32bit":

                  os.environ['PATH'] += ";C:\\SAPRFCSDK\\32bit"

                  SAPNWRFC = "C:\\apps\\portal\\sapapi\\nwrfcsdk\\lib\\sapnwrfc.dll"

                elif str(platform.architecture()[0]) == "64bit":

                  os.environ['PATH'] += ";C:\\SAPRFCSDK\\64bit"

                  SAPNWRFC = "C:\\apps\\portal\\sapapi\\nwrfcsdk\\lib\\sapnwrfc.dll"

 

                SAP = windll.LoadLibrary(SAPNWRFC)

 

                #-Prototypes------------------------------------------------------------

                SAP.RfcAppendNewRow.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcAppendNewRow.restype = c_void_p

 

                SAP.RfcCloseConnection.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcCloseConnection.restype = c_ulong

 

                SAP.RfcCreateFunction.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcCreateFunction.restype = c_void_p

 

                SAP.RfcCreateFunctionDesc.argtypes = [c_wchar_p, POINTER(ErrInf)]

                SAP.RfcCreateFunctionDesc.restype = c_void_p

 

                SAP.RfcDestroyFunction.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcDestroyFunction.restype = c_ulong

 

                SAP.RfcDestroyFunctionDesc.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcDestroyFunctionDesc.restype = c_ulong

 

                SAP.RfcGetChars.argtypes = [c_void_p, c_wchar_p, c_void_p, c_ulong, \

                  POINTER(ErrInf)]

                SAP.RfcGetChars.restype = c_ulong

 

                SAP.RfcGetCurrentRow.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcGetCurrentRow.restype = c_void_p

 

                SAP.RfcGetFunctionDesc.argtypes = [c_void_p, c_wchar_p, POINTER(ErrInf)]

                SAP.RfcGetFunctionDesc.restype = c_void_p

 

                SAP.RfcGetRowCount.argtypes = [c_void_p, POINTER(c_ulong), \

                  POINTER(ErrInf)]

                SAP.RfcGetRowCount.restype = c_ulong

 

                SAP.RfcGetStructure.argtypes = [c_void_p, c_wchar_p, \

                  POINTER(c_void_p), POINTER(ErrInf)]

                SAP.RfcGetStructure.restype = c_ulong

 

                SAP.RfcGetTable.argtypes = [c_void_p, c_wchar_p, POINTER(c_void_p), \

                  POINTER(ErrInf)]

                SAP.RfcGetTable.restype = c_ulong

 

                SAP.RfcGetVersion.argtypes = [POINTER(c_ulong), POINTER(c_ulong), \

                  POINTER(c_ulong)]

                SAP.RfcGetVersion.restype = c_wchar_p

 

                SAP.RfcInstallServerFunction.argtypes = [c_wchar_p, c_void_p, \

                  c_void_p, POINTER(ErrInf)]

                SAP.RfcInstallServerFunction.restype = c_ulong

 

                SAP.RfcInvoke.argtypes = [c_void_p, c_void_p, POINTER(ErrInf)]

                SAP.RfcInvoke.restype = c_ulong

 

                SAP.RfcListenAndDispatch.argtypes = [c_void_p, c_ulong, POINTER(ErrInf)]

                SAP.RfcListenAndDispatch.restype = c_ulong

 

                SAP.RfcMoveToFirstRow.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcMoveToFirstRow.restype = c_ulong

 

                SAP.RfcMoveToNextRow.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcMoveToNextRow.restype = c_ulong

 

                SAP.RfcOpenConnection.argtypes = [POINTER(ConnParams), c_ulong, \

                  POINTER(ErrInf)]

                SAP.RfcOpenConnection.restype = c_void_p

 

                SAP.RfcPing.argtypes = [c_void_p, POINTER(ErrInf)]

                SAP.RfcPing.restype = c_ulong

 

                SAP.RfcRegisterServer.argtypes = [POINTER(SConParams), c_ulong, \

                  POINTER(ErrInf)]

                SAP.RfcRegisterServer.restype = c_void_p

 

                SAP.RfcSetChars.argtypes = [c_void_p, c_wchar_p, c_wchar_p, c_ulong, \

                  POINTER(ErrInf)]

                SAP.RfcSetChars.restype = c_ulong

 

                #-Connection parameters-------------------------------------------------

                RfcConnParams[0].name = "ASHOST"; RfcConnParams[0].value = "saptep52.tenaris.ot"

                RfcConnParams[1].name = "SYSNR" ; RfcConnParams[1].value = "52"

                RfcConnParams[2].name = "CLIENT"; RfcConnParams[2].value = "800"

                RfcConnParams[3].name = "USER"           ; RfcConnParams[3].value = "SVCSAPAPI"

                RfcConnParams[4].name = "PASSWD"; RfcConnParams[4].value = ""

 

                TableName = "/TENR/T_PLANNED"

                versi = ""

                od = ""

                oddis = ""

                customer = ""

                truck = ""

                charBuffer1 = ""

                description = ""

                urcs = []

                hRFC = SAP.RfcOpenConnection(RfcConnParams, 5, RfcErrInf)

                if hRFC != None:

                                charBuffer = create_unicode_buffer(512 + 1)

                                hFuncDesc = SAP.RfcGetFunctionDesc(hRFC, "RFC_READ_TABLE", RfcErrInf)

                                if hFuncDesc != 0:

 

                                                hFunc = SAP.RfcCreateFunction(hFuncDesc, RfcErrInf)

 

                                                if hFunc != 0:

 

                                                                rc = SAP.RfcSetChars(hFunc, "QUERY_TABLE", TableName, len(TableName), RfcErrInf)

                                                                rc = SAP.RfcSetChars(hFunc, "DELIMITER", "~", 1, RfcErrInf)

 

                                                                hFields = c_void_p(0)

                                                                rc = SAP.RfcGetTable(hFunc, "FIELDS", hFields, RfcErrInf)

                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "VERSI", 5, RfcErrInf)

                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "TUBE_BAR_CODE", 13, RfcErrInf)

                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "TRAID", 5, RfcErrInf)

                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "CARRI", 5, RfcErrInf)

                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "ODDIS", 5, RfcErrInf)

                                               

                                                                hOptions = c_void_p(0)

                                                                if SAP.RfcGetTable(hFunc, "OPTIONS", hOptions, RfcErrInf ) == RFC_OK:

                                                                                hRow = SAP.RfcAppendNewRow(hOptions, RfcErrInf)

                                                                                description = "TUBE_BAR_CODE = '" + urc + "'"

                                                                                rc = SAP.RfcSetChars(hRow, "TEXT", description, len(description),RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hFunc, "ROWCOUNT", "100", 3, RfcErrInf)

 

                                                                if SAP.RfcInvoke(hRFC, hFunc, RfcErrInf) == RFC_OK:

                                                                                hTable = c_void_p(0)

                                                                                if SAP.RfcGetTable(hFunc, "DATA", hTable, RfcErrInf) == RFC_OK:

                                                                                                RowCount = c_ulong(0)

                                                                                                rc = SAP.RfcGetRowCount(hTable, RowCount, RfcErrInf)

                                                                                                rc = SAP.RfcMoveToFirstRow(hTable, RfcErrInf)

                                                                                                for i in range(0, RowCount.value):

                                                                                                                hRow = SAP.RfcGetCurrentRow(hTable, RfcErrInf)

                                                                                                                rc = SAP.RfcGetChars(hRow, "WA", charBuffer, 512, RfcErrInf)

                                                                                                                my_list = charBuffer.value.split("~")

                                                                                                                versi = my_list[0].replace(" ","")

                                                                                                                truck = my_list[2].replace(" ","")

                                                                                                                customer = my_list[3].strip()

                                                                                                                oddis = my_list[4].replace(" ","")

                                                                                                                if i < RowCount.value:

                                                                                                                                rc = SAP.RfcMoveToNextRow(hTable, RfcErrInf)

                                                                rc = SAP.RfcDestroyFunction(hFunc, RfcErrInf)

 

 

                                                                hFunc = SAP.RfcCreateFunction(hFuncDesc, RfcErrInf)

                                                                if hFunc != 0:

 

                                                                                rc = SAP.RfcSetChars(hFunc, "QUERY_TABLE", TableName, len(TableName), RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hFunc, "DELIMITER", "~", 1, RfcErrInf)

 

                                                                                hFields = c_void_p(0)

                                                                                rc = SAP.RfcGetTable(hFunc, "FIELDS", hFields, RfcErrInf)

                                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "VERSI", 5, RfcErrInf)

                                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "TUBE_BAR_CODE", 13, RfcErrInf)

                                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "TRAID", 5, RfcErrInf)

                                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "CARRI", 5, RfcErrInf)

                                                                                hRow = SAP.RfcAppendNewRow(hFields, RfcErrInf)

                                                                                rc = SAP.RfcSetChars(hRow, "FIELDNAME", "ODDIS", 5, RfcErrInf)

                                                               

                                                                                hOptions = c_void_p(0)

                                                                                if SAP.RfcGetTable(hFunc, "OPTIONS", hOptions, RfcErrInf ) == RFC_OK:

                                                                                                hRow = SAP.RfcAppendNewRow(hOptions, RfcErrInf)

                                                                                                description = "VERSI = '" + versi + "'"

                                                                                                rc = SAP.RfcSetChars(hRow, "TEXT", description, len(description),RfcErrInf)

                                                                                                rc = SAP.RfcSetChars(hFunc, "ROWCOUNT", "100", 3, RfcErrInf)

 

                                                                                if SAP.RfcInvoke(hRFC, hFunc, RfcErrInf) == RFC_OK:

                                                                                                hTable = c_void_p(0)

                                                                                                if SAP.RfcGetTable(hFunc, "DATA", hTable, RfcErrInf) == RFC_OK:

                                                                                                                f = open("Output.txt", "w+")

                                                                                                                RowCount = c_ulong(0)

                                                                                                                rc = SAP.RfcGetRowCount(hTable, RowCount, RfcErrInf)

                                                                                                                rc = SAP.RfcMoveToFirstRow(hTable, RfcErrInf)

                                                                                                                for i in range(0, RowCount.value):

                                                                                                                                hRow = SAP.RfcGetCurrentRow(hTable, RfcErrInf)

                                                                                                                                rc = SAP.RfcGetChars(hRow, "WA", charBuffer, 512, RfcErrInf)

                                                                                                                                my_list = charBuffer.value.split("~")

                                                                                                                                urcs.append(my_list[1].replace(" ",""))

                                                                                                                                charBuffer1 = ",".join(str(x).strip() for x in my_list)

                                                                                                                                f.write(charBuffer1 + '\n')

                                                                                                                                if i < RowCount.value:

                                                                                                                                                rc = SAP.RfcMoveToNextRow(hTable, RfcErrInf)

                                                                                                                urcs = set(urcs)

                                                                                                                urcs = list(urcs)

                                                                                                                urcs.sort()

                                                                                rc = SAP.RfcDestroyFunction(hFunc, RfcErrInf)

 

 

                                rc = SAP.RfcCloseConnection(hRFC, RfcErrInf)

 

                else:

                                with open("debugsapresponse.log","a") as f:

                                                f.write(RfcErrInf.key+","+RfcErrInf.message+"\n")

                                                f.close

#                             print(RfcErrInf.key)

#                             print(RfcErrInf.message)

 

                del SAP

               

                return {

                'od': versi.lstrip('0'),

                'truck': truck.upper(),

                'customer': customer[:21],

                'urcs': urcs,

                'count': len(urcs),

                'oddis': oddis.lstrip('0')

                }

 

                #-End-------------------------------------------------------------------

 

 