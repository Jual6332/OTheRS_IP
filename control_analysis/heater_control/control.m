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

    dt = t - time_last;
    time_last = t;

    % Sum error over all time
    integral_err = integral_err + (Ttgt - T)*dt;

    Qdot = Kp * (Ttgt - T) + Ki * integral_err;
    Qdot = max([Qdot, 0]); % require Qdot to greater than or equal to zero
end
