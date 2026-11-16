
% Financial Statement Data
% Dashes in the original statement are represented as zero.

data = [
    0          0          410        0          0          410;
    -8223      -1159      -7268      -7440      -7795      -31885;
    -8223      -1159      -6858      -7440      -7795      -31475;
    -434491    -447226    -711194    -801774    -734604    -3129289;
    201944     245745     0          44433      326402     818524;
    201944     245745     0          44433      326402     818524;
    -232547    -201481    -711194    -757341    -408202    -2310765;
    4488995    4314545    4249816    3538622    2781281    19373259;
    58097      136752     0          0          -4540      190309;
    4547092    4451297    4249816    3538622    2776741    19563568;
    4314545    4249816    3538622    2781281    2368539    17252803
    ];

% Create MATLAB Table
rowNames = {
    'Gain_Loss_on_Sale'
    'Interest_Expense'
    'Total_Non_Operating'
    'Income_Before_Transfers'
    'Operating_Grants'
    'Total_Contributions'
    'Change_in_Net_Position'
    'Beginning_Net_Position'
    'Restatement'
    'Restated_Beginning_Position'
    'Ending_Net_Position'
    };

T = array2table(data, ...
    'VariableNames', {'2021','2022','2023', ...
    '2024','2025','Total'}, ...
    'RowNames', rowNames);

% Display Table
disp(T);

% Extract data for bar graph (first five years)
income = data(4,1:5);
grants = data(5,1:5);
change = data(7,1:5);

% Create Grouped Bar Graph
graphData = [income' grants' change'];

figure;

bar(graphData);

title('Financial Performance by Year');
xlabel('Year');
ylabel('Amount ($)');

xticklabels({'2021','2022','2023','2024',['2025']});

legend('Income Before Transfers', ...
    'Operating Grants', ...
    'Change in Net Position', ...
    'Location','best');

yline(0, 'k-');

grid on;



