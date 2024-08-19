
from db import DB
import pandas as pd
from departmentAnalysis import DepartmentAnalysis

# Conexión a la base de datos
db = DB()
db.connect_DB()

# Consulta a la base de datos
query = 'SELECT * FROM EmployeePerformance'
employees_data = db.Query(query)

# Cerrar conexión a la base de datos
db.close_DB()

# Crear DataFrame
df = pd.DataFrame(employees_data, columns=['id', 'employee_id', 'department', 'performance_score', 'years_with_company', 'salary'])


analysis = DepartmentAnalysis(df)
analysis.calculate_statistics()
analysis.calculate_correlations()
analysis.print_statistics()
analysis.plot_histograms()
analysis.plot_scatter()