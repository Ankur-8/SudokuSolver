from flask import Flask, request, render_template
import solver  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Extract the Sudoku grid from the form data
    grid = request.form.getlist('cell')
    grid = [int(cell) if cell else 0 for cell in grid]
    
    # Reshape the grid to a 9x9 matrix
    grid = [grid[i:i + 9] for i in range(0, len(grid), 9)]
    
    # Solve the Sudoku puzzle using the solver
    solution = solver.solve(grid)
    return render_template('solution.html', solution=solution)

if __name__ == '__main__':
    app.run()
