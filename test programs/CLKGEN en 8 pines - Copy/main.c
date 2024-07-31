#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "pico/binary_info.h"
#include "hardware/pio.h"
#include "clock.pio.h"


#define PIO_CLOCK_PIN 0
//#define PIO_FREQ_DIVIDER 25 //2.5 or 2[MHz]
#define PIO_FREQ_DIVIDER 50 //1.25 or 1[MHz]

int main() {
    stdio_init_all();
	set_sys_clock_khz(125000, true);
	//set_sys_clock_khz(100000, true); //How to change base clk
	PIO pioInstance = pio0;
	uint pioOffset = pio_add_program(pioInstance, &clock_program);
	uint pioStateMachine = pio_claim_unused_sm(pioInstance, true);
	// This auxiliary function initializes the PIO and starts running it with the information passed.
	clock_program_init(pioInstance, pioStateMachine, pioOffset, PIO_CLOCK_PIN, PIO_FREQ_DIVIDER);
	
    while (1) {
		
    }
}
