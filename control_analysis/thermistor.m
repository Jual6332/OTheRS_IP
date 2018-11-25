% Find the optimimum second resistor for a 10K thermistor
clear all; clc;

Vin = 3.3;
Tmax =  60;
Tmin = -30;

ADC_BITS = 10;
ADC_resolution = Vin/(2^ADC_BITS -1);

% Load data between Tmin and Tmax
data = load('./temperatures');
idx  = Tmin <= data(:, 1) & data(:, 1) <= Tmax;
data = data(Tmin <= data(:, 1) & data(:, 1) <= Tmax, :);
resistance_range = linspace(1e2, 1e5, 1e4);

min_max_temp_reading = zeros(length(resistance_range), 2);

for i = 1:length(resistance_range)
    R1 = resistance_range(i);
    
    % -30 degC
    Rth = data(1, 2) * 1e3;
    output_voltage = Vin*(Rth/(Rth+R1));
    min_max_temp_reading(i, 1) = output_voltage;

    % 60 degC
    Rth = data(end, 2) * 1e3;
    output_voltage = Vin*(Rth/(Rth+R1));
    min_max_temp_reading(i, 2) = output_voltage;
end

% Find the resistor R1 that gives the widest voltage range across the relevant temperatures
voltage_range = min_max_temp_reading(:, 1) - min_max_temp_reading(:, 2);
[maxval, idx] = max(voltage_range);
ideal_resistance = resistance_range(idx);

fprintf('Ideal resistance %d kOhms\n', ideal_resistance/1000);

figure; hold on; grid on;
title('Voltage Range vs Resistor Value');
xlabel('R1 Resistance (\Omega)');
ylabel('Output Voltage');

semilogx(resistance_range, min_max_temp_reading(:, 1), 'b', ... 
                        'displayname', 'Voltage at -30 degC')
semilogx(resistance_range, min_max_temp_reading(:, 2), 'r', ... 
                        'displayname', 'Voltage at 60 degC')
semilogx(resistance_range, voltage_range, 'g', ... 
                        'linewidth', 2, ... 
                        'displayname', 'Voltage Range')
legend('show')

plot(ideal_resistance, maxval, 'ro')

