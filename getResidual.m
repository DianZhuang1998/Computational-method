
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [residual] = getResidual(data, coeffs)
  y = data;
  p = length(coeffs);
  N = length(y);
  e = zeros(1, N - p);
  a = zeros(1, p + 1);
  a(1) = 1;
  for i = 2 : p + 1
    a(i) = coeffs(i - 1);
  end
  e = filter(a, 1, y);
  residual = e;
end

