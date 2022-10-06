# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:55:33 2022

@author: as292
"""

regList = ["RCC_AHBENR", "RCC_APB2ENR", "RCC_APB1ENR"]
        
setAHB  = ('0','1','2','4','6','8','10')

setAPB1 = ('0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','11'
           ,'14','15','17','18','19','20','21','22','23','25'
           ,'27','28','29')

setAPB2 = ('0 ','2 ','3 ','4 ','5 ','6 ','7 ',
           '8 ','9 ','10','11','12','13','14',
           '15','19','20','21')

def RCC_SystemClock():
        
    print ("------------System Clock ------------")
    
    # reset file
    rcc = open("RCC_config.c", 'w')
    rcc.write(" ")
    rcc.close()
    
    
    rcc = open("RCC_config.c", 'a')
    rcc.write("void RCC_voidInitSysClock (void)\n{\n")
    
    # RCC_CLOCK_TYPE parameter
    print("RCC clock Type:")
    print("1. High Speed External Crystal")
    print("2. High Speed External RC")
    print("3. High Speed Internal (8MHz)")
    print("4. PLL enable ")
    
    rccClockType = str(input("Type: "))
    
    if rccClockType == '1':
        rcc.write("\n\tSET_BIT(RCC_CR, RCC_CR_HSE_ON);")
        rcc.write("\n\twhile (!(GET_BIT(RCC_CR,	RCC_CR_HSE_RDY)));")
        rcc.write("\n\tRCC_CFGR = 0x00000001;")
    
    elif rccClockType == '2':
        rcc.write("\n\tSET_BIT(RCC_CR, RCC_CR_HSE_ON);")
        rcc.write("\n\twhile (!(GET_BIT(RCC_CR,	RCC_CR_HSE_RDY)));")
        rcc.write("\n\tSET_BIT(RCC_CR, RCC_CR_HSE_BYP);")
        rcc.write("\n\tRCC_CFGR = 0x00000001;")
    
    elif rccClockType == '3':
        rcc.write("\n\tSET_BIT(RCC_CR,	RCC_CR_HSI_ON);")
        rcc.write("\n\twhile (!(GET_BIT(RCC_CR,	RCC_CR_HSI_RDY)));")
        rcc.write("\n\tRCC_CFGR = 0x00000000;")
        
    
    elif rccClockType == '4':
        rcc.write("\n\tSET_BIT(RCC_CR,	RCC_CR_PLL_ON);")
        
        # RCC_PLL_INPUT parameter
        print("PLL clock parameter: ")
        print("1. Enable Enable to HSI/2")
        print("2. Enable Enable HSE/2")
        print("3. Enable Enable HSE")
        
        rccPLL = str(input("Type: "))
        
        if rccPLL == '1':
            rcc.write("\\ntSET_BIT(RCC_CR, RCC_CR_HSI_ON);")
        elif rccPLL == '2':
            rcc.write("\n\tSET_BIT(RCC_CR, RCC_CR_HSE_ON);")
        elif rccPLL == '3':
            rcc.write("\n\tSET_BIT(RCC_CR, RCC_CR_HSE_ON);")
        else :
            print("Invalid RCC PLL INPUT ")
        # RCC_PLL_MUL_VAL parameter
        print("PLL Multiplication Factor :\n(take care not to exceed the maximum processor Clock)")
        rccPLL_mull = str(input("Value (2:16): "))
        
        if int(rccPLL_mull) >= 2 and int(rccPLL_mull) <= 16:
            rcc.write("\n\tRCC_CFGR = ((RCC_CFGR & RCC_CFGR_PLLMUL_MASK)|(RCC_PLL_MUL_VAL-2));")
        else :
            print("Invalid Multiplication Factor")
    else :
        print("Invalid Clock Type")
        rcc.close();
        rcc = open("RCC_config.c", 'w')
        rcc.write(" ")
    rcc.write("\n}")
    rcc.close();
    
def RCC_disableClockPerephiral ():
    print("------------Disable Clock For Prepirals------------")
    rcc = open("RCC_config.c", 'a')
    
    
    rcc.write("\n\nvoid RCC_voidDisableClock ( void ){\n")
    while (True):
        print ("0. DMA1\t Direct Memory Access Module 1")
        print ("1. DMA2\t Direct Memory Access Module 2")
        print ("2. SRAM\t Static RAM")
        print ("3. FLITF\tFlash memory Interface")
        print ("4. CRC")
        print ("5. FSMC")
        print ("6. SDIO")
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X':
            rcc.write("\n\tCLR_BIT( "+ regList[0] + "	,"+ setAHB[int(choise)] +");")
        elif choise == 'X':
            break
    
    while (True):
            
        print ("0. TIM2		")		
        print ("1. TIM3		")
        print ("2. TIM4		")
        print ("3. TIM5		")
        print ("4. TIM6		")
        print ("5. TIM7		")
        print ("6. TIM12	")
        print ("7. TIM13	")
        print ("8. TIM14	")
        print ("9. WWDG		")
        print ("10. SPI2	")
        print ("11. SPI3	")
        print ("12. USART2	")
        print ("13. USART3	")
        print ("14. USART4	")
        print ("15. USART5	")
        print ("16. I2C1	")
        print ("17. I2C2	")
        print ("18. USB		")
        print ("19. CAN		")
        print ("20. BKP		")
        print ("21. PWR		")
        print ("22. DAC		")
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X' and int(choise)<=22:
            rcc.write("\n\tCLR_BIT( "+ regList[1]   +","+ setAPB1[int(choise)] +");")
        elif choise == 'X':
            break
        
    while (True):
            
        print('0.  AFIO	')
        print('1.  IOPA	')
        print('2.  IOPB	')
        print('3.  IOPC	')
        print('4.  IOPD	')
        print('5.  IOPE	')
        print('6.  IOPF	')
        print('7.  IOPG	')
        print('8.  ADC1	')
        print('9.  ADC2	')
        print('10. TIM1	')
        print('11. SPI1	')
        print('12. TIM8	')
        print('13. USART1')
        print('14. ADC3	')
        print('15. TIM9	')
        print('16. TIM10')
        print('17. TIM11')
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X' and int(choise)<=17:
            rcc.write("\n\tCLR_BIT( "+ regList[2]   +","+ setAPB2[int(choise)] +");")
        elif choise == 'X':
            rcc.write("\n\n}");
            rcc.close();
            break

def RCC_enableClockPerephiral ():
    print("------------Enable Clock For Prepirals------------")
    print("Enable Clock for peripherals:")

    rcc = open("RCC_config.c", 'a')


    rcc.write("\n\nvoid RCC_voidEnableClock ( void ){\n")
    while (True):
        print ("0. DMA1\t Direct Memory Access Module 1")
        print ("1. DMA2\t Direct Memory Access Module 2")
        print ("2. SRAM\t Static RAM")
        print ("3. FLITF\tFlash memory Interface")
        print ("4. CRC")
        print ("5. FSMC")
        print ("6. SDIO")
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X':
            rcc.write("\n\tSET_BIT( "+ regList[0]  +" ,"+ setAHB[int(choise)] +");")
        elif choise == 'X':
            break

    while (True):
            
        print ("0. TIM2		")		
        print ("1. TIM3		")
        print ("2. TIM4		")
        print ("3. TIM5		")
        print ("4. TIM6		")
        print ("5. TIM7		")
        print ("6. TIM12	")
        print ("7. TIM13	")
        print ("8. TIM14	")
        print ("9. WWDG		")
        print ("10. SPI2	")
        print ("11. SPI3	")
        print ("12. USART2	")
        print ("13. USART3	")
        print ("14. USART4	")
        print ("15. USART5	")
        print ("16. I2C1	")
        print ("17. I2C2	")
        print ("18. USB		")
        print ("19. CAN		")
        print ("20. BKP		")
        print ("21. PWR		")
        print ("22. DAC		")
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X' and int(choise)<=22:
            rcc.write("\n\tSET_BIT( "+ regList[1]   +","+ setAPB1[int(choise)] +");")
        elif choise == 'X':
            break
        
    while (True):
            
        print('0.  AFIO	')
        print('1.  IOPA	')
        print('2.  IOPB	')
        print('3.  IOPC	')
        print('4.  IOPD	')
        print('5.  IOPE	')
        print('6.  IOPF	')
        print('7.  IOPG	')
        print('8.  ADC1	')
        print('9.  ADC2	')
        print('10. TIM1	')
        print('11. SPI1	')
        print('12. TIM8	')
        print('13. USART1')
        print('14. ADC3	')
        print('15. TIM9	')
        print('16. TIM10')
        print('17. TIM11')
        print ("x. Skip")
        
        
        choise = str(input("Peripheral ID: ")).upper()
        
        if choise != 'X' and int(choise)<=17:
            rcc.write("\n\tSET_BIT( "+ regList[2]   +","+ setAPB2[int(choise)] +");")
        elif choise == 'X':
            rcc.write("\n\n}");
            rcc.close();
            break


