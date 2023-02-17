
clear all
clc

% Parameter setting
sourceAudio = 'source_squabb';
N = 2048;                % param N: length of block
hopSize = 1024;          % param H: window overlap (samples)
p = 10;                  % param p: AR model order               

detThresh = 4;           % param detThresh: threshold for click detection               
detStretch = 4;          % param detStretch: amount to stretch detection boundaries
numIter = 5;             % param numIter: amount of iterations for iterative optimizations

% audio read
[x, fs] = audioread([sourceAudio, '.wav']);  
audiowrite(['degraded.wav'],x, fs);

secs = 10;
x_new = x(1:fs*secs,:);
audiowrite(['input.wav'],x_new, fs);

n=length(x_new);

%% Add click noise
tt =(1:n);
T = 1/fs;%Sampling interval
t = (0:n-1)*T;%Time axis
f = (0:n-1)/n*fs;%Frequency axis

noise=0.02*cos(8000*2*pi/fs*tt');%Click Noise
s_noise=fft(noise,n);
abs_noise=abs(s_noise);
figure;
subplot(2,1,1); plot(t,noise);   
xlabel('Time/s');ylabel('Amplitude');
title('Noise time domain waveform');  grid on;
subplot(2,1,2); 
plot(f,abs_noise);
title('Noise power spectrum');

s=x_new+noise;%Add noise


audiowrite(['myclean.wav'],s, fs);


[x_restore, ~] = ARdeclick(x_new, p, N, hopSize, detThresh, detStretch, numIter);

display('done');

audiowrite(['restored.wav'],x_restore, fs);
audiowrite(['output.wav'],x_restore, fs);

[coeffs_i, avg_i] = estimateARcoeffs(x_new, p);
res_i = getResidual(x_new - avg_i, coeffs_i);
[coeffs_n, avg_n] = estimateARcoeffs(x_restore, p);
res_n = getResidual(x_restore - avg_n, coeffs_n);

figure;
plot(x_new(:,1)); 
hold on
plot(x_restore(:,1)); 
xlabel('Audio signal in time domain');
ylabel('Amplitude');
legend('Input degraded signal','Output restored signal')
title('Input degraded signal vs Output restored signal')



figure,
plot(res_i(:,1));
hold on
plot(res_n(:,1));
legend('Input degraded signal','Output restored signal')
title('Predict error')
