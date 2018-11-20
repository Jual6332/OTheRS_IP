% Run a PID control law here
function Qdot = control(T, t, Ttgt, Kp, Kd, Ki)
    % TODO: Actually do the formal analysis and find the right gains
    % TODO: All the logic for differential control

    % Define a stateful variable here, which will maintain its
    % value between calls
    global integral_err;
    if isempty(integral_err)
        integral_err = 0;
    end

    global time_last;
    if isempty(time_last)
        time_last = 0;
    end

    persistent last_measurement;
    if isempty(last_measurement)
        last_measurement = 0;
    end

    dt = t - time_last;
    time_last = t;


    % Calculate derivative
    delta = last_measurement - T;
    last_measurement = T;
    derivative = delta / dt;
    % Protect against a dt of 0
    if dt == 0
        derivative = 0;
    end

    % Sum error over all time
    integral_err = integral_err + (Ttgt - T)*dt;

    Qdot = Kp * (Ttgt - T) ...   % Proportional
         + Ki * integral_err ... % Integral
         + Kd * derivative;      % Derivative
end
