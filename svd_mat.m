format long e
addpath(genpath('../src_hpfem'))
% ns 359 180 90 45 23
% delf1 5 10 20 40 80
% delf2 25 50 100 200 400

% -----------------------------------------------------------
customName = false;

% if no custom name, enter the samples etc.
% marcos
del_f1 = 1;
del_f2 = 3;
s1 = 10:del_f1:1000;
s2 = 1000:del_f2:5000;
sample = [s1, s2(1:end-1)];


% evenly spaced
% sample = linspace(5, 5000, 180);

% interpolated sample
% N_o = 2500;
% sample = linspace(10, 5000, N_o);


N_s = length(sample)
nModes = 20;
% -----------------------------------------------------------

if customName == true
    customFileName = input('Enter SVD file name in array folder: SVDResult_', 's')
    fileName = ['arrays/SVDResult_',customFileName]
else
    fileName = ['arrays/SVDResult_Ns',num2str(N_s),'_m',num2str(nModes)]
end

load(fileName,'H','S','G');

fprintf("size of H: (%d, %d) \n", size(H))
fprintf("size of S: (%d, %d) \n", size(S))
fprintf("size of G: (%d, %d) \n", size(G))
fprintf("size of conj G: (%d, %d) \n", size(conj(G)))
% G is complex double
% NS=( 180 90 45 23 )
% F1=( 10 20 40 80 )
% F2=( 50 100 200 400 )

    
fprintf("size of snapshots: (%d, %d) \n", size(sample))
y = complex2cols(conj(G));
fprintf("size of G' as [real, complex]: (%d, %d) \n", size(y))
if customName == true
    customSaveName = input('Enter the save name: X_y_', 's')
    saveName = ['arrays/X_y_', customSaveName]
    save(saveName, 'sample', 'y')
else
    if nModes == 20
        save(['arrays/X_y_',num2str(N_s),'.mat'], 'sample', 'y')
    else
        save(['arrays/X_y_',num2str(N_s),'_m',num2str(nModes),'.mat'], 'sample', 'y')
    end
end