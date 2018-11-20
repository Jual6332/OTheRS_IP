#include <iostream>
#include <string>
#include <errno.h>
#include <cstdint>
#include <unistd.h>
#include <wiringPiSPI.h>

#include "thermocouple.h"


const int CHANNEL = 0;

int main(int argc, char* argv[]) {
    int fd;
    uint8_t buffer[4] = {0};

    fd = wiringPiSPISetup(CHANNEL, 500000);

    if (fd > 0) {
        while(true) {
            wiringPiSPIDataRW(CHANNEL, buffer, sizeof(buffer));
            MAX31855K max = MAX31855K::from_bytes_le(buffer);
            std::cout << max.display() << std::endl;
            sleep(1);
        }
    }
}
