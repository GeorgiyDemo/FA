package com.demka;

import java.io.FileWriter;
import java.io.IOException;


class Solver {


    double[] expValues;
    int size;

    public Solver(int size) {
        this.size = size;
        this.expValues = new double[size];
    }

    public void expression(int iteration, double r, double x) {

        double result = r * x * (1 - x);

        expValues[iteration] = result;
        iteration++;
        if (iteration < this.size) {
            expression(iteration, r, result);
        }
    }

    public double[] getValues() {
        return this.expValues;
    }
}


class WriteToFile {
    public static void main(String str) {
        try {
            FileWriter myWriter = new FileWriter("./out.txt");
            myWriter.write(str);
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}

public class Main {


    public static void main(String[] args) {

        int N = 200;

        Solver solver = new Solver(N);
        solver.expression(0, 2.6, 0.4);
        double[] bufresult = solver.getValues();

        String[] result = new String[N];
        for (int i = 0; i < bufresult.length; i++) {
            result[i] = String.valueOf(bufresult[i]);
        }

        String joined = String.join("\n", result);
        WriteToFile file = new WriteToFile();
        file.main(joined);

    }
}
