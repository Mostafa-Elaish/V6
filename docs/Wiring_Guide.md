# Jarvis Wiring Guide

## Core Wiring
- **Raspberry Pi 5 (16GB)** with SSD HAT + 256GB SSD
- **Camera**: Pi HD camera via CSI ribbon cable
- **Touchscreen**: 7” official display via DSI, power from 5V GPIO rail or USB
- **Microphone**: USB mic (plug & play)
- **Speaker**: USB or 3.5mm jack

## Motors & Movement
- **Omni-wheels** controlled via motor driver (L298N or similar)
- Motor driver powered from separate 12V PSU, **shared ground** with Pi

## Sensors
- **Ultrasonic**: TRIG on GPIO23, ECHO on GPIO24
- **PIR motion**: GPIO17
- **Temperature & Humidity (DHT22)**: GPIO4
- **Light Sensor (LDR via ADC)**: MCP3008 on SPI pins
- **RGB LED**: GPIO18 (PWM)

## Notes
- Use 5V/5A rated supply for Pi + peripherals
- Fuse protection for motors
- Keep camera ribbon away from motor wires (noise)