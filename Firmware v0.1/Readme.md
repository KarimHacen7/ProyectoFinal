<h1> Proyecto Final </h1>
<p>This repository contains the RP2040's firmware.</p>

<h3> COMANDOS Interfaz con PC </h3>
<h4> Muestreo Digital </h4>
<p>
    #ABCDEFGHI; 
        Donde:
            A: D, Muestreo Digital
            B: 0-4, Modo de Gatillado, 0 para no gatillado
            C: Canal de gatillado 1-8
            D: Numero de canales: 8, 4, 2, 1
            EF: 00-16, Frecuencia de Muestreo, ver tabla de verdad
            GHI: 000-192, Profundidad de Muestreo, en KiB
</p>
<h4>Muestreo Analógico</h4>
<p>
    #ABCDEFGHI; 
        Donde:
            A: A, Muestreo Analógico
            B: 0-4, Modo de Gatillado, 0 para no gatillado
            C: Canal de gatillado 8
            D: Numero de canales: 1
            EF: 00-13, Frecuencia de Muestreo, ver tabla de verdad
            GHI: 000-192, Profundidad de Muestreo, en KiB
</p>
<h3>Configurar</h3>
<h4>Voltaje Referencia</h4>
        #ABCDE; //sin \n
            Donde:
                A: C, Configurar
                B: V, Voltaje DAC
                CDE: Voltaje, Formato "C.DE" [V]
<h4>Temporizador Gatillados</h4>        
        #ABCDEF; //sin \n
            Donde:
                A: C, Configurar
                B: T, Timeout
                CDE: Tiempo, Formato "CDEF"x10 [ms]

/* TODO:
	Profundidad de muestreo:
		en bytes 1-192, con paso de 1
	Frecuencias de Muestreo:
		Digital
			125 MHz	16
			100 MHz*15
			50 MHz*	14
			25 MHz	13
			10 MHz*	12
			5 MHz	11
			2 MHz	10
			1 MHz	09
			500 KHz	08
			250 KHz	07
			100 KHz	06
			50 KHz	05
			25 KHz	04
			10 KHz	03
			5 KHz	02
			2.5 KHz	01
			1 KHz	00
		Analógico
			25 MHz	13
			10 MHz* 12
			5 MHz	11
			2 MHz	10
			1 MHz	09
			500 KHz	08
			250 KHz	07
			100 KHz	06
			50 KHz	05
			25 KHz	04
			10 KHz	03
			5 KHz	02
			2,5 KHz	01
			1 KHz	00
	Modos de Funcionamiento:
		Digital
			Untriggered Sampling                            0
				8 Canales
				4 Canales
				2 Canales
				1 Canal
			Triggered Sampling
				8 Canales
					Flanco Subida                           1
					Flanco Bajada                           2
					Nivel Bajo                              3
					Nivel Alto                              4
				4 Canales
					Flanco Subida                           1
					Flanco Bajada                           2
					Nivel Bajo                              3
					Nivel Alto                              4
				2 Canales
					Flanco Subida                           1
					Flanco Bajada                           2
					Nivel Bajo                              3
					Nivel Alto                              4
				1 Canal
					Flanco Subida                           1
					Flanco Bajada                           2
					Nivel Bajo                              3
					Nivel Alto                              4
		Analógico
			Untriggered Sampling                        0
			Triggered Sampling
				Flanco Subida                           1
                Flanco Bajada                           2
                Nivel Bajo     							3
                Nivel Alto     							4
		Configurar
			Voltaje Referencia
			Timeout Triggers
	
	


Futuras mejoras firmware:
	Poner para poder editar el tiempo en alto y el tiempo en bajo de los flancos.
	Poner para gatillar con un canal que no sea el de muestreo.
	Poner para cambiar los canales que se muestean (contiguos) se puedan mover.

Futuras mejoras hardware:
	Poner comparadores MAX9201 para mayor tolerancia a tension de entrada (implica cambiar el suministro a fuentes partidas) y mucho mayor ancho de banda.
	Poner ADCs como MAX1312 para mayor tolerancia a tension de entrada, (ver de usar uno con mayor velocidad de conversion).
	Poner los putos fusibles no?
	Poner una tarjeta de memoria para guardar los datos. (implica overclock para llegar a data rates decentes, aun usando SDIO).
	PASATE A UNA PLATAFORMA MEJOR. (Bottleneck en el USB).
*/