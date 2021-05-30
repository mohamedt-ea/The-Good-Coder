int motor1a = 2;    // Motor 1 pin1
int motor1b = 3;    // Motor 1 pin2
int motor1_speed = ; // enable pin for motor 1 ENB1

int motor2a = 4;    // Motor 2 Pin1
int motor2b = 5;    // Motor 2 pin2
int motor2_speed = ; // ENB2

char dir = 'S'; //direction
int speed = 0 ; //speed

void setup() {
  // put your setup code here, to run once:
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    char bluetooth_reading = Serial.read();
    read_bluetooth(bluetooth_reading);
    bot_control(dir, speed);

}

// motor control - speed control
/*
    Clockwise - Anticlockwise

    dirction: char
        C --> clockwise
        A --> Anticlockwise
    motor: int 
        {1, 2}
    speed: int 
        0-255
*/
void motor_control(char direction, int motor, int speed)
{
    switch (direction)
    {
        case 'c':
            if(motor == 1)
            {
                digitalWrite(motor1a, HIGH);
                digitalWrite(motor1b, LOW);
                analogWrite(motor1_speed, speed);
            }else if(motor == 2)
            {
                digitalWrite(motor2a, HIGH);
                digitalWrite(motor2b, LOW);
                analogWrite(motor2_speed, speed);  
            }
            break;

        case 'a':
            if(motor == 1)
            {
                digitalWrite(motor1a, LOW);
                digitalWrite(motor1b, HIGH);
                analogWrite(motor1_speed, speed);
            }else if(motor == 2)
            {
                digitalWrite(motor2a, LOW);
                digitalWrite(motor2b, HIGH);
                analogWrite(motor2_speed, speed);
            }
            break;
         case 's':
            digitalWrite(motor1a, LOW);
            digitalWrite(motor1b, LOW);
            break;

    }

}



// Bot control
/* 
    dirction : char
        F --> forward
        B --> Backward
        R --> Right
        L --> Left
    speed : int 

*/
void bot_control(char direction, int speed)
{
    switch(direction)
    {
        case'F':
            motor_control( 'c', 1, speed);
            motor_control( 'c', 2, speed);
        break;

        case'B':
            motor_control( 'a', 1, speed);
            motor_control( 'a', 2, speed);
        break;

        case'L':
            motor_control( 'c', 1, speed);
            motor_control( 'c', 2, speed);

        break;
        case'R':
            motor_control( 'c', 1, speed);
            motor_control( 'c', 2, speed);

        break;

        case 'S':
            motor_control( 's', 1, speed);
            motor_control( 's', 2, speed);
    }
}

// speed converter
int speed_converter(char speed_symbol)
{
    if(speed_symbol >= '0' && speed_symbol <= '4')
    {
        return 75;
    }else if(speed_symbol >= '5' && speed_symbol <= '7')
    {
        return 127;
    }else if(speed_symbol >= '8' && speed_symbol <= '9')
    {
        return 200;
    }else if(speed_symbol == 'q')
    {
        return 255;
    }
}


// control 
void read_bluetooth(char reading)
{
        switch(reading)
    {
        case 'F':
            dir = 'F';
        break; 
        case 'R':
            dir = 'R';
        break;
        case 'L':
            dir = 'L';
        break;
        case 'S':
            dir = 'S';
        break;
        case 'B':
            dir = 'B';
        break;
        case '0':
            speed = speed_converter('0');
        break;
        case '1':
            speed = speed_converter('1');
        break;
        case '2':
            speed = speed_converter('2');
        break;
        case '3':
            speed = speed_converter('3');
        break;
        case '4':
            speed = speed_converter('4');
        break;
        case '5':
            speed = speed_converter('5');
        break;
        case '6':
            speed = speed_converter('6');
        break; 
        case '7':
            speed = speed_converter('7');
        break;
        case '8':
            speed = speed_converter('8');
        break;
        case '9':
            speed = speed_converter('9');
        break;
        case 'q':
            speed = speed_converter('q');
        break;  
    }
}


// Blutooth transmission
void read_from_blutooth()
{


}

// IR - Ultrasonic 




