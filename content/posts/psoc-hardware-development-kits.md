---
tags:
- bluetooth
- cypress
- hardware
- microcontroller
- example project
- documentation
- development kit
title: PSoC 4 Hardware Development Kits
---

There are several [Cypress](http://www.cypress.com/) [Programmable System on a Chip (PSoC®)](http://www.cypress.com/products/programmable-system-chip-psoc) hardware development kits available for use in designs. The list below describes strengths of each kit and provides links to documentation.

1.  [PSoC® 4 Bluetooth® Low Energy (BLE) Pioneer Kit (CY8CKIT-042-BLE-A)](http://www.cypress.com/documentation/development-kitsboards/cy8ckit-042-ble-bluetooth-low-energy-42-compliant-pioneer-kit)

**Strength:** Easy-to-use Bluetooth that can be connected to other devices

**Documentation**

-   [Bluetooth® Low Energy (BLE) Pioneer Kit Guide](http://www.cypress.com/file/234851/download) from Cypress.
-   [PSoC® 4 BLE Module](http://www.cypress.com/documentation/development-kitsboards/cy8ckit-142-psoc-4-ble-module) (includes information on connecting external power up to 5V)
-   [PSoC® 4200 Family Datasheet](http://www.cypress.com/documentation/datasheets/psoc-4-psoc-4200-family-datasheet-programmable-system-chip-psoc)

**Example Projects:** [100 Projects in 100 Days with PSoC® 4 BLE](http://www.cypress.com/blog/100-projects-100-days) from Cypress

**Availability:** Check out in PRLTA 109 or buy from [Newark](http://www.newark.com/cypress-semiconductor/cy8ckit-042-ble/dev-board-psoc-4-bluetooth-low/dp/92X9232?ost=CY8CKIT-042-BLE).

[PSoC® 4 Pioneer Kit (CY8CKIT-042)](http://www.cypress.com/documentation/development-kitsboards/cy8ckit-042-psoc-4-pioneer-kit)

**Strength:** Compatible with Arduino shields

**Documentation**

-   [Pioneer Kit Guide](http://www.cypress.com/file/46056/download) from Cypress. Includes information on power connections.
-   [Pioneer Kit Dimensions](https://drive.google.com/file/d/0ByRWb7dgVD-rVVU5Mm04bEZLd3c/edit?usp=sharing)
-   [PSoC® 4200 Family Datasheet](http://www.cypress.com/documentation/datasheets/psoc-4-psoc-4200-family-datasheet-programmable-system-chip-psoc)

**Example Projects:** [100 Projects in 100 Days with PSoC® 4 Pioneer Kit](http://www.element14.com/community/thread/23736/l/100-projects-in-100-days) from element14

**Availability:** Check out in PRLTA 109 or buy from [Newark](http://www.newark.com/cypress-semiconductor/cy8ckit-042/dev-kit-psoc-4-pioneer-arduino/dp/69W7455?ost=CY8CKIT-042&categoryId=800000004005).

[PSoC® 4 Prototyping Kit (CY8CKIT-049)](http://www.cypress.com/documentation/development-kitsboards/psoc-4-cy8ckit-049-4xxx-prototyping-kits)

**Strength:** Small size

**Documentation**

-   [Prototyping Kit Guide](http://www.cypress.com/file/141306/download) from Cypress. Includes information on power connections.

**Availability:** Check out in PRLTA 109 or buy from [Newark](http://www.newark.com/cypress-semiconductor/cy8ckit-049-42xx/prototype-board-cy8c42xx-family/dp/39X7573).

[PSoC® 5LP Development Kit (CY8CKIT-050)](http://www.cypress.com/documentation/development-kitsboards/cy8ckit-050-psoc-5lp-development-kit)

**Strengths:** More processing power and I/O pins than the PSoC® 4, LCD display

**Documentation**

-   [Development Kit Guide](http://www.cypress.com/file/45276/download) from Cypress. Includes information on power connections.

**Availability:** Check out from [Dr. Jordan](mailto:shawn.s.jordan@asu.edu) or buy from [Newark](http://www.newark.com/cypress-semiconductor/cy8ckit-050/psoc-5-cy8c55-capsense-lcd-display/dp/58T0044?ost=CY8CKIT-050&categoryId=800000004005).

## How many PSoC® chips does the PSoC® 4 Pioneer Kit have?

As shown in the block diagram in Figure 1 (below), the PSoC® 4 Pioneer Kit has two PSoC® chips on it: a PSoC® 4 (where you download and run your code on) and a PSoC® 5LP (which is used to program the PSoC® 4). Your computer connects to the USB Mini B port, which communicates with the PSoC® 5LP, which programs the PSoC® 4. For more information on the Pioneer Kit architecture, see the Theory of Operation section in the [PSoC® 4 Pioneer Kit Guide](http://www.cypress.com/?docID=47035).

  -------------------------------------
  ![](/figures/figure_345.jpg){class="img-fluid"}
  Figure 1: Pioneer Kit Block Diagram
  -------------------------------------
