import matplotlib.pyplot as plt


class DepartmentAnalysis:
    def __init__(self, df):
        self.df = df
        self.grouped = df.groupby('department')
    
    def calculate_statistics(self):
        self.mean_performance = self.grouped['performance_score'].mean()
        self.mean_salary = self.grouped['salary'].mean()
        self.median_performance = self.grouped['performance_score'].median()
        self.median_salary = self.grouped['salary'].median()
        self.std_performance = self.grouped['performance_score'].std()
        self.std_salary = self.grouped['salary'].std()
        self.total_employees = self.grouped['employee_id'].count()
    
    def calculate_correlations(self):
        self.correlation_years_performance = self.df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
        self.correlation_salary_performance = self.df[['salary', 'performance_score']].corr().iloc[0, 1]
    
    def print_statistics(self):
        print("Media del performance_score por departamento:\n", self.mean_performance)
        print("Mediana del performance_score por departamento:\n", self.median_performance)
        print("Desviación estándar del performance_score por departamento:\n", self.std_performance)
        print("Media del salary por departamento:\n", self.mean_salary)
        print("Mediana del salary por departamento:\n", self.median_salary)
        print("Desviación estándar del salary por departamento:\n", self.std_salary)
        print("Número total de empleados por departamento:\n", self.total_employees)
        print("Correlación entre years_with_company y performance_score:", self.correlation_years_performance)
        print("Correlación entre salary y performance_score:", self.correlation_salary_performance)
    
    def plot_histograms(self):
        for department, data in self.grouped:
            plt.figure()
            self.df[self.df['department'] == department]['performance_score'].hist()
            plt.title(f'Histograma del performance_score para {department}')
            plt.xlabel('Performance Score')
            plt.ylabel('Frecuencia')
            plt.show()
    
    def plot_scatter(self):
        plt.figure()
        plt.scatter(self.df['years_with_company'], self.df['performance_score'])
        plt.title('Grafico de dispersión de years_with_company vs. performance_score')
        plt.xlabel('Years with Company')
        plt.ylabel('Performance Score')
        plt.show()

        plt.figure()
        plt.scatter(self.df['salary'], self.df['performance_score'])
        plt.title('Grafico de dispersión de salary vs. performance_score')
        plt.xlabel('Salary')
        plt.ylabel('Performance Score')
        plt.show()
