function [dT] = linear_odefn(t, y, m, cp, T0, Kc, Kr, control_fn)
% linear_odefn: Linearized model of the heater dynamics
% Arguments:
%          t:          Timestep, seconds
%          y:          Ode45's state vector, this only only contains delta T, the
%                      temperature difference from the point linearized about
%          m:          Mass of the heater, kg
%          cp:         Specific heat
%          T0:         Temperature which to linearize about
%          Kc:         Conduction heat loss coeff
%          Kr:         Radiation heat loss coeff
%          control_fn: closed loop control function, of the
%                      form Qdot_in = control_fn(dT, t)

    sigma = 1.380649e-23; % J * K−1 boltzmann constant
    dT = y(1);

    % sum of the heat flows
    QdotC = -Kc*dT;                % conduction
    QdotR = -(4*Kr*sigma*T0^3)*dT; % radiation
    QdotE = control_fn(dT, t);     % control

    dT = (QdotC + QdotR + QdotE) / (m*cp);
end
