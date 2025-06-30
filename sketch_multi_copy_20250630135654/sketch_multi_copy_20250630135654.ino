#define MODE_2x4  // ← 若要切换为2x2模式，请注释掉这一行

#ifdef MODE_2x4
const int ROWS = 2;
const int COLS = 4;
int rowPins[ROWS] = {12, 14};
int colPins[COLS] = {34, 35, 32, 33};
#else
const int ROWS = 2;
const int COLS = 2;
int rowPins[ROWS] = {12, 14};
int colPins[COLS] = {32, 33};
#endif

int rawValues[ROWS][COLS] = {0};

struct CalibrationCoefficients {
    float a, b, c, d;
};

const CalibrationCoefficients COMMON_CALIB = {
    -5.045e-10,
    4.384e-06,
    -0.014,
    18.057
};

CalibrationCoefficients calib[ROWS][COLS];

void setup() {
    Serial.begin(115200);

    for (int i = 0; i < ROWS; i++) {
        pinMode(rowPins[i], OUTPUT);
        digitalWrite(rowPins[i], LOW);
    }

    for (int j = 0; j < COLS; j++) {
        pinMode(colPins[j], INPUT);
    }

    for (int r = 0; r < ROWS; r++) {
        for (int c = 0; c < COLS; c++) {
            calib[r][c] = COMMON_CALIB;
        }
    }
}

float calculateResistance(int adcValue, int row, int col) {
    auto k = calib[row][col];
    return k.a * adcValue * adcValue * adcValue +
           k.b * adcValue * adcValue +
           k.c * adcValue +
           k.d;
}

void loop() {
    for (int row = 0; row < ROWS; row++) {
        digitalWrite(rowPins[row], HIGH);
        delayMicroseconds(50);

        for (int col = 0; col < COLS; col++) {
            rawValues[row][col] = analogRead(colPins[col]);
        }

        digitalWrite(rowPins[row], LOW);
    }

    String resistString = "";
    for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
            resistString += String(rawValues[row][col]);
            if (!(row == ROWS - 1 && col == COLS - 1)) {
                resistString += ",";
            }
        }
    }
    Serial.println(resistString);

    delay(200);
}
