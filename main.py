
from db import connect_DB
import pandas as pd
import matplotlib.pyplot as plt
db = connect_DB()
try:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM EmployeePerformance')
    employees_data = cursor.fetchall()
    cursor.close()
    db.close()
    df = pd.DataFrame(employees_data, columns=['id', 'employee_id', 'department', 'performance_score', 'years_with_company', 'salary'])
except Exception as e:
    print('Error : %s' % e)
    db.rollback()
    db.close()

# Calcular estadisticas por departamento
grouped = df.groupby('department')

# Media
mean_performance = grouped['performance_score'].mean()
mean_salary = grouped['salary'].mean()

# Mediana
median_performance = grouped['performance_score'].median()
median_salary = grouped['salary'].median()

# Desviacion estandar
std_performance = grouped['performance_score'].std()
std_salary = grouped['salary'].std()

# Numero total de empleados por departamento
total_employees = grouped['employee_id'].count()

# Correlaciones
correlation_years_performance = df[['years_with_company', 'performance_score']].corr().iloc[0, 1]
correlation_salary_performance = df[['salary', 'performance_score']].corr().iloc[0, 1]


print("Media del performance_score por departamento:\n", mean_performance)
print("Mediana del performance_score por departamento:\n", median_performance)
print("Desviación estándar del performance_score por departamento:\n", std_performance)
print("Media del salary por departamento:\n", mean_salary)
print("Mediana del salary por departamento:\n", median_salary)
print("Desviación estándar del salary por departamento:\n", std_salary)
print("Número total de empleados por departamento:\n", total_employees)
print("Correlación entre years_with_company y performance_score:", correlation_years_performance)
print("Correlación entre salary y performance_score:", correlation_salary_performance)

# Visualizacion de datos

# Histograma del performance_score para cada departamento.
for department, data in grouped:
    plt.figure()
    df[df['department'] == department]['performance_score'].hist()
    plt.title(f'Histograma del performance_score para {department}')
    plt.xlabel('Performance Score')
    plt.ylabel('Frecuencia')
    plt.show()
    
# Gráfico de dispersión de years_with_company vs. performance_score.
plt.figure()
plt.scatter(df['years_with_company'], df['performance_score'])
plt.title('Grafico de dispersión de years_with_company vs. performance_score')
plt.xlabel('Years with Company')
plt.ylabel('Performance Score')
plt.show()

# Gráfico de dispersión de salary vs. performance_score.
plt.figure()
plt.scatter(df['salary'], df['performance_score'])
plt.title('Grafico de dispersión de salary vs. performance_score')
plt.xlabel('Salary')
plt.ylabel('Performance Score')
plt.show()