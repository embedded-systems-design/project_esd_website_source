---
title: Common Pin Types and their Meanings
---

Modified from [here](https://docs.kicad.org/6.0/en/eeschema/eeschema.html#pin-electrical-types)

| Pin Type       | Description                                                                                                                                                                                      |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input          | A pin which is exclusively an input.                                                                                                                                                             |
| Output         | A pin which is exclusively an output.                                                                                                                                                            |
| Bidirectional  | A pin that can be either an input or an output, such as a microcontroller data bus pin.                                                                                                          |
| Tri-state      | A three state output pin (high, low, or high impedance)                                                                                                                                          |
| Passive        | A passive symbol pin: resistors, connectors, etc.                                                                                                                                                |
| Free           | A pin that can be freely connected to any other pin without electrical concerns.                                                                                                                 |
| Unspecified    | A pin for which the ERC check does not matter.                                                                                                                                                   |
| Power input    | A symbol’s power pin. As a special case, power input pins that are marked invisible are automatically connected to the net with the same name. See the Power Ports section for more information. |
| Power output   | A pin that provides power to other pins, such as a regulator output.                                                                                                                             |
| Open collector | An open collector logic output.                                                                                                                                                                  |
| Open emitter   | An open emitter logic output.                                                                                                                                                                    |
| Unconnected    | A pin that should not be connected to anything.                                                                                                                                                  |
