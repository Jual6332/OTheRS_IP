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
data = data(idx, :);
datalen = length(data);
resistance_range = linspace(1e3, 1e5, 1e3);

differentials = zeros(length(resistance_range), 1);
min_max_temp_reading = zeros(length(resistance_range), 2);

for i = 1:length(resistance_range)
    min_volt = 0;
    max_volt = 0;
    R1 = resistance_range(i);
    % for j = 1:datalen % Every data point
    %     Rth = data(j, 2) * 1e3; % thermistor resistance
    %     output_voltage = Vin*(Rth/(Rth+R1));
    %     min_volt = min([min_volt, output_voltage]);
    %     max_volt = max([max_volt, output_voltage]);
    % end
    
    % -30 degC
    Rth = data(1, 2) * 1e3;
    output_voltage = Vin*(Rth/(Rth+R1));
    min_max_temp_reading(i, 1) = output_voltage;

    % 60 degC
    Rth = data(end, 2) * 1e3;
    output_voltage = Vin*(Rth/(Rth+R1));
    min_max_temp_reading(i, 2) = output_voltage;

    differentials(i) = max_volt - min_volt;
    % ADC_reading(i) = ceil(max_volt ./ ADC_resolution);
end




voltage_range = min_max_temp_reading(:, 1) - min_max_temp_reading(:, 2);

[maxval, idx] = max(voltage_range);
ideal_resistance = resistance_range(idx);
fprintf('Ideal resistance %d kOhms\n', ideal_resistance/1000);


figure; hold on; grid on;
title('Voltage Range vs Resistor Value');
xlabel('log_{10}(R1) Resistance (log_{10}(\Omega))');
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

