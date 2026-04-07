pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build stage executed"'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 - <<EOF
import calculator

print("Running Calculator Tests...")

print("Testing add:")
print("2 + 3 =", calculator.add(2,3))
assert calculator.add(2,3) == 5

print("Testing subtract:")
print("5 - 3 =", calculator.subtract(5,3))
assert calculator.subtract(5,3) == 2

print("Testing multiply:")
print("2 * 3 =", calculator.multiply(2,3))
assert calculator.multiply(2,3) == 6

print("Testing divide:")
print("6 / 3 =", calculator.divide(6,3))
assert calculator.divide(6,3) == 2

print("All tests passed successfully!")
EOF
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploy stage placeholder"'
            }
        }
    }
}
