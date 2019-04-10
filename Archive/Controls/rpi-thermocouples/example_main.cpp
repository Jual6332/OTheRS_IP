#include <iostream>
#include <bitset>
#include <string>
#include <errno.h>
#include <cstdint>
#include <unistd.h>
#include <wiringPiSPI.h>

#include "Max31855kReading.h"

const int CHANNEL = 0;

int main(int argc, char* argv[]) {
    int fd;
    uint8_t buffer[4] = {0};

    fd = wiringPiSPISetup(CHANNEL, 500000);

    if (fd > 0) {
        while(true) {
            wiringPiSPIDataRW(CHANNEL, buffer, sizeof(buffer));
            Max31855kReading max = Max31855kReading::from_bytes_le(buffer);
            std::cout << max.display() << std::endl;
            sleep(1);
        }
    }
}
