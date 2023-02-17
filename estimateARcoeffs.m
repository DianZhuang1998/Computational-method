
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [coeffs, avg] = estimateARcoeffs(data, model_order)
  N = length(data);
  P = model_order;
  y = data;
  R = zeros(P, P);
  r = zeros(P, 1);
  for i = 1 : P
    for j = 1 : P
        R(i, j) = sum(y(P + 1 - j : N - j) .* y(P + 1 - i : N - i));
        r(i) = sum(y(P + 1 : N) .* y(P + 1 - i : N - i)); 
    end
  end
  coeffs = -R \ r;
  avg = mean(data(P + 1 : N));
end