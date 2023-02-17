function [i] = clickdetect(ehat, stdhat,detThresh, detStretch)

% returns indices of detected noise

% widen so indices don't go out of bounds.
i_temp = [zeros(detStretch,1); abs(ehat) > detThresh*stdhat; zeros(detStretch,1)];
i = zeros(length(ehat),1);


for k = 1:length(ehat)
    i(k) = any(i_temp(k:k+2*detStretch));
end

end