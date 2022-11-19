;Configuración de Microcontrolador -----------------------------------------------------------
LIST P=16F877A
RADIX HEX
#include <p16F877a.inc>
;---------------------------------------------------------------------------------------------
		
		
;Configuración de Hardware (Configuration Word)-----------------------------------------------
__CONFIG  _CP_OFF &_WDTE_OFF & _PWRTE_OFF & _HS_OSC & _CPD_OFF & _LVP_OFF & _BOREN_OFF & _WRT_OFF & _DEBUG_OFF

 
CONT		EQU 0X31
RESULTADO1  EQU 0X50

 ; INICIO DEL PROGRAMA
        ORG       0x00                         ; VECTOR DE INICIO
        GOTO      INICIO                       ; IR A INICIO
        ;SE CONFIGURAON LOS PUERTOS
       ORG  0x05

INICIO
		CLRW                                    ;LIMPIA REGISTRO W

		BANKSEL PORTA
		CLRF    PORTA
        CLRF    PORTB
        CLRF    PORTC
        CLRF    PORTD

;==========================================================================================
;===============================CONFIGURACION DE PUERTOS =================================
;==========================================================================================
	

		BANKSEL  TRISA                          ;SELECCION DE BANCO
		CLRF     TRISA                          ;SE LIMPIA REGISTRO 
        MOVLW    B'00111111'                    ;SE CONFIGURAON I/O 
        MOVWF    TRISA
        MOVLW    B'00000000'                    ;SE CONFIGURAN I/O ENTRADAS Y SALIDAS DIGITALES
        MOVWF    TRISB
        MOVLW    B'10011111'
        MOVWF    TRISC                          ;PORTC SALIDAS
	    MOVLW    B'10000000'                     ;SE CONFIGURAN I/O ENTRADAS Y SALIDAS DIGITALES
        MOVWF    TRISD                          
	
	
	

;======================================================================================
;=====================CONFIGURACION CONVERTIDOR ANALOGICO DIGITAL======================
;======================================================================================


;REGISTRO ADCON0
; |ADCS1|ADCS0|CHS2|CHS1|CHS0|GO/DONE|-|ADON|

		BANKSEL  ADCON0
		MOVLW    B'10000001'                ;(RA0/AN0)
		MOVWF    ADCON0
		CALL     DELAY



;;REGISTRO ADCON1
; |ADF|-|-|-|PCFG3|PCFG2|PCFG1|PCFG0|

		BANKSEL  ADCON1
		MOVLW    B'00000100'        ;D AN7/RE2,D AN6/RE1,D AN5/RE0,D AN4/RA5,A AN3/RA3,D AN2/RA2,A AN1/RA1,A AN0/RA0 (VDD)
		MOVWF    ADCON1




;==========================================================================================
;============================CONFIGURACION COMUNICACION SERIAL USART=======================
;==========================================================================================

  
        ;BCF      TRISC,6                       ;RC6/TX SALIDA, PIN DE TRANSMMISION
        ;BSF      TRISC,7                       ;RC7/RX ENTRADA, PIN RECEPCION
        MOVLW    D'6'                           ;9600 BAUD RATE XTAL= 4MHz
        MOVWF    SPBRG
        BCF      TXSTA,BRGH                     ;SELECCION DE BAJA VELOCIDAD (0)
        BCF      TXSTA,SYNC                    ;MODO ASINCRONO (0)

        BCF      STATUS,RP0                    ;IR AL BANCO 0
        BCF      STATUS,RP1      

        BSF      RCSTA,SPEN                    ;HABILITA EL PUERTO SERIAL
        
		BSF      STATUS,RP0                    ;IR AL BANCO 1
        BCF      STATUS,RP1 

        BCF      TXSTA,TX9                     ; 8 BITS DE DATOS PARA TRANSMISION
        BSF      TXSTA,TXEN                    ;ACTIVA LA TRANSMISION SERIAL TXIF=1
         

        BANKSEL   RCSTA
        BCF      RCSTA,RX9                     ; 8 BITS DE DATOS
        BSF      RCSTA,CREN                    ;PARA RX CONTINUO



;======================================================================================
;====================SUB RUTINA CONVERTIDOR ANALOGICO DITIAL=============================
;=======================================================================================

ADC_1
	     BSF     ADCON0,GO   ;START A/D CONVERSION

_ESPERA
         BTFSC   ADCON0,GO  ;ADCON0 ES 0 O LA CONVERSION ESTA COMPLETA? 
         GOTO    _ESPERA    ;NO IR _ESPERA
         MOVFW   ADRESH    ;W=ADDRESH
         MOVWF   TXREG      ;TXREG = W TRANSMITE DATO
         MOVWF   PORTB
         MOVFW   ADRESL    ;W=ADDRESL
         MOVWF   PORTD

_ESPERATX
  
         BTFSS   PIR1,TXIF    ;ESPERA QUE TERMINE DE TRANSMITIR
         GOTO    _ESPERATX
         GOTO    ADC_1

DELAY
    	CLRF 	 CONT
    	MOVLW 	 0A  ;COLOCA 200 EN EL CONTADOR
	    MOVWF 	 CONT
CICLO1
	    DECF 	 CONT, 1	;DECREMENTA HASTA QUE SEA CERO Y SALE DEL CICLO
	    BTFSS 	 STATUS, Z
	    GOTO     CICLO1
	
	RETURN


     END
