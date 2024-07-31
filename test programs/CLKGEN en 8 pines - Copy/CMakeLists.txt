cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(CLKGEN_en_8_pines)

pico_sdk_init()

add_executable(${PROJECT_NAME})

pico_generate_pio_header(${PROJECT_NAME} ${CMAKE_CURRENT_LIST_DIR}/clock.pio)

target_sources(${PROJECT_NAME} PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/main.c
        )

pico_enable_stdio_usb(${PROJECT_NAME} 1)

# pull in common dependencies and additional spi hardware support, plus PIO
target_link_libraries(${PROJECT_NAME} 
                pico_stdlib 
                hardware_pio
                )

# create map/bin/hex file etc.
pico_add_extra_outputs(${PROJECT_NAME})

