"""
----------------------------------------------------
------ Author: Ayman Saleh        ------------------ 
------ Date  : 6/OCT/2022         ------------------ 
------ Version: V.1.0.1           ------------------ 
------ Type   : Main configuration Tool   ---------- 
----------------------------------------------------

"""

#   inport RCC configuration Module
import RCC_configTool


RCC_configTool.RCC_SystemClock()
RCC_configTool.RCC_enableClockPerephiral()
RCC_configTool.RCC_disableClockPerephiral()