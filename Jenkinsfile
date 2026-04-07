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

print("Testing sub:")
print("5 - 3 =", calculator.sub(5,3))
assert calculator.sub(5,3) == 2

print("Testing mul:")
print("2 * 3 =", calculator.mul(2,3))
assert calculator.mul(2,3) == 6

print("Testing div:")
print("6 / 3 =", calculator.div(6,3))
assert calculator.div(6,3) == 2

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
