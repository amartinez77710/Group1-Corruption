% Village of Cuba Water & Sewer Financials (2021-2025)
years = 2021:2025;
revenues = [405565, 421905, 412235, 504557, 496658] / 1e3; % in $K
expenses = [831833, 867972, 1116571, 1298891, 1223467] / 1e3; % in $K
deficit  = [426268, 446067, 704336, 794334, 726809] / 1e3; % in $K

figure('Color', 'w', 'Position', [100, 100, 950, 420]);

% Panel 1: Operating Revenues vs. Total Operating Expenses
subplot(1, 2, 1);
b = bar(years, [revenues; expenses]', 'grouped');
b(1).FaceColor = [0.18, 0.49, 0.72]; % Blue for Revenue
b(2).FaceColor = [0.84, 0.24, 0.21]; % Red for Expenses
title('Operating Revenues vs. Expenses', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('USD ($ Thousands)', 'FontSize', 10);
legend({'Operating Revenues', 'Total Operating Expenses'}, 'Location', 'northwest');
grid on;
ylim([0 1500]);

% Panel 2: Escalating Annual Operating Deficit
subplot(1, 2, 2);
b2 = bar(years, deficit, 0.55, 'FaceColor', [0.45, 0.15, 0.15]);
title('Annual Utility Operating Loss (2021–2025)', 'FontSize', 12, 'FontWeight', 'bold');
ylabel('Operating Loss ($ Thousands)', 'FontSize', 10);
grid on;
ylim([0 950]);

% Add exact dollar labels above deficit bars
for i = 1:length(years)
    text(years(i), deficit(i) + 25, sprintf('$%.0fK', deficit(i)), ...
        'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'FontSize', 9);
end

sgtitle('Village of Cuba Water & Sewer Financial Deficit ($3.10M Total Loss)', ...
    'FontSize', 14, 'FontWeight', 'bold');