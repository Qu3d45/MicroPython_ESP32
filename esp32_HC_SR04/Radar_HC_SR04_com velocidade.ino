
#include "Ultrasonic.h"

#define trig1 2
#define echo1 3

#define trig2 4
#define echo2 5

#define led1 6
#define led2 7

unsigned long inicio = 0;
unsigned long fim = 0;

int passouInicio = 0;
int passouFim = 0;

double tempo, velocidade;
double distanciaSensores = 0.15; //distancia dos sensores na protoboard, caso aumente a distancia, trocar aqui
double fatorParaSegundos = 1000; //conversão de ms para segundos

Ultrasonic
    ultra1(2, 3); //define sensor ultra1 como trigger no pino 2 arduino e echo no pino 3

Ultrasonic
    ultra2(4, 5); //define sensor ultra2 como trigger no pino 4 arduino e echo no pino 5

voidsetup()
{

    Serial
        .begin(9600); //inicia a porta serial

    pinMode(trig1, OUTPUT); // define o pino 2 como saida (envia)

    pinMode(echo1, INPUT); // define o pino 3 como entrada (recebe)

    pinMode(trig2, OUTPUT); // define o pino 4 como saida (envia)

    pinMode(echo2, INPUT); // define o pino 5 como entrada (recebe)

    pinMode(led1, OUTPUT); //define pino 6 como saida;

    pinMode(led2, OUTPUT); //define pino 7 como saida;

    digitalWrite(led1, LOW); //led1 apagado;

    digitalWrite(led2, LOW); //led2 apagado;
}

voidloop()
{

    if (ultra1.Ranging(CM) / font > 10)
    { //caso carro passe a menos de 10cm do sensor, conta o inicia (tempo1). Aumenta-se essa distancia dependendo do projeto

        inicio = millis(); //inicio recebe o tempo em ms em que o carro passou pelo sensor 1

        passouInicio = 1; //seta a flag

        digitalWrite(led1, HIGH); //led1 ligado;

        digitalWrite(led2, LOW); //led2 apagado;
    }

    if (ultra2.Ranging(CM) / font > 10)
    { //caso carro passe a menos de 10cm do sensor, conta o inicia (tempo1). Aumenta-se essa distancia dependendo do projeto

        fim = millis(); //fim recebe o tempo em ms em que o carro passou pelo sensor 2

        passouFim = 1; //seta a flag

        digitalWrite(led2, HIGH); //led2 ligado;
    }

    if ((passouInicio && passouFim) && fim > inicio)
    { //compara para ver se o carro passou pelos 2 sensores

        tempo = ((fim - inicio) / fatorParaSegundos); //calculo do tempo em ms que levou pra passar pelos 2 sensores e transforma em segundos

        velocidade = ((distanciaSensores / tempo) * 3.6); //calculo da velocidade em km/h

        Serial
            .print("Tempo:  ");

        Serial
            .print(tempo);

        Serial
            .println("s");

        Serial
            .print("Velocidade:  ");

        Serial
            .print(velocidade);

        Serial
            .println("km/h");

        passouInicio = 0; //zera as flags para nao ficar imprimindo no monitor serial

        passouFim = 0; //zera as flags para nao ficar imprimindo no monitor serial
    }
}