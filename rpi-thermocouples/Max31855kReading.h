#include <sstream>
#include <string>
#include <errno.h>
#include <cstdint>
#include <wiringPiSPI.h>


// A simple class for the data from a MAX31855K thermocouple chip
// this class does not handle the SPI communication
// TODO: Cold junction temperature compensation reading
class Max31855kReading {
public:
    Max31855kReading(uint32_t data) {
        oc_fault  = data        & 1; // D0
        scg_fault = (data >> 1) & 1; // D1
        scv_fault = (data >> 2) & 1; // D2
        reserved2 = (data >> 3) & 1; // D3 always 0

        // 12 bit internal temperature (bits 4:15)
        raw_internal_temp = (data >> 4) & 0b0000111111111111;

        fault = (data >> 16) & 1; // D16
        reserved1 = (data >> 17) & 1; // D16 always 0


        /* the block below is shamelessly copied from sparkfun code. This kind of bitmath is beyond me */
        // Bits D[31:18] are the signed 14-bit thermocouple temperature value
        if (data & ((uint32_t)1 << 31)) { // Sign extend negative numbers
            raw_temp = 0xC000 | ((data >> 18) & 0x3FFF);
        } else {
            raw_temp = data >> 18; // Shift off all but the temperature data
        }

        // FIXME
        // temp = raw_temp / 4.0; // convert to degC
        // internal_temp = raw_internal_temp / 4.0; // convert to degC
    }

    // construct from 4 bytes, little endian
    static
    Max31855kReading from_bytes_le(uint8_t *bytes) {
        return Max31855kReading(bytes_to_uint_le(bytes));
    }

    // construct from 4 bytes, big endian
    static
    Max31855kReading from_bytes_be(uint8_t *bytes) {
        return Max31855kReading(bytes_to_uint_be(bytes));
    }

    std::string display() {
        std::ostringstream stream;
        stream << temp_degC() << " degrees C";
        // various faults
        if (is_scv_fault()) {
            stream << "\nSCV FAULT";
        }
        if (is_scg_fault()) {
            stream << "\nSCG FAULT";
        }
        if (is_oc_fault()) {
            stream << "\nOC FAULT";
        }
        if (is_all_zeros()) {
            stream << "\nWARNING: all data in packet is zero. "
                "Is the breakout board plugged in?";
        }
        return stream.str();
    }

    // shorted to vcc
    bool is_scv_fault() {
        return scv_fault == 1;
    }

    // shorted to ground
    bool is_scg_fault() {
        return scg_fault == 1;
    }

    // open circuit
    bool is_oc_fault() {
        return oc_fault == 1;
    }

    bool is_all_zeros() {
        return raw_temp          == 0
            && reserved1         == 0
            && fault             == 0
            && raw_internal_temp == 0
            && reserved2         == 0
            && scv_fault         == 0
            && scg_fault         == 0
            && oc_fault          == 0;
    }

    // temperature in celcius
    double temp_degC() {
        return (raw_temp / 4.0);
    }

    // temperature in freedomheit
    double temp_degF() {
        return (raw_temp / 4.0)*(9.0/5.0) + 32;
    }

private:
    // double   temp;
    // double   internal_temp;
    uint16_t raw_temp;
    uint8_t  reserved1;
    uint8_t  fault;
    uint16_t raw_internal_temp;
    uint8_t  reserved2;
    uint8_t  scv_fault;
    uint8_t  scg_fault;
    uint8_t  oc_fault;

    static
    uint32_t bytes_to_uint_be(uint8_t *buffer) {
        uint32_t result = 0;
        result = (buffer[3] << 24)
               | (buffer[2] << 16)
               | (buffer[1] << 8 )
               | (buffer[0]);
        return result;
    }

    static
    uint32_t bytes_to_uint_le(uint8_t *buffer) {
        uint32_t result = 0;
        result = (buffer[0] << 24)
               | (buffer[1] << 16)
               | (buffer[2] << 8 )
               | (buffer[3]);
        return result;
    }
};


