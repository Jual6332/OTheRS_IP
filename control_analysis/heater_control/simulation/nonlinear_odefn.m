function [dT] = nonlinear_odefn(t, y, m, cp, Tsurr, Kc, Kr, control_fn)
% nonlinear_odefn: Full model of the heater dynamics
% Arguments:
%          t:          Timestep, seconds
%          y:          Ode45's state vector, this only only contains delta T, the
%                      temperature difference from the point linearized about
%          m:          Mass of the heater, kg
%          cp:         Specific heat
%          Tsurr:      Temperature of the ambient environment
%          Kc:         Conduction heat loss coeff
%          Kr:         Radiation heat loss coeff
%          control_fn: closed loop control function, of the
%                      form Qdot_in = control_fn(T, t)
    sigma = 1.380649e-23; % J * K−1 boltzmann constant
    T = y(1);

    % sum of the heat flows
    QdotC = -Kc*(T - Tsurr);           % conduction
    QdotR = -Kr*sigma*(T^4 - Tsurr^4); % radiation
    QdotE = control_fn(T, t);          % control
    QdotE = max([QdotE, 0]); % Clamp at zero

    dT = (QdotC + QdotR + QdotE) / (m*cp);
end
