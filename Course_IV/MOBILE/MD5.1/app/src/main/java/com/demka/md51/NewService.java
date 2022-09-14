package com.demka.md51;

import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.os.Message;
import android.util.Log;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class NewService extends Service {
    private static Timer timer;
    private Context ctx;
    private static final String TAG = "TimerService";

    public IBinder onBind(Intent arg0) {
        Log.v(TAG, "onBind called");
        return null;
    }

    public void onCreate() {
        Log.v(TAG, "onCreate called");
        super.onCreate();
        ctx = this;
        startService();
    }

    private void startService() {
        Log.v(TAG, "startService called");
        timer = new Timer();
        timer.scheduleAtFixedRate(new mainTask(), 0, 4000);
    }

    private class mainTask extends TimerTask {
        public void run() {
            toastHandler.sendEmptyMessage(0);
        }
    }

    public void onDestroy() {
        Log.v(TAG, "onDestroy called");
        super.onDestroy();
        Toast.makeText(this, "Service stopped..", Toast.LENGTH_SHORT).show();
        timer.cancel();
    }

    private final Handler toastHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            Date currentTime = Calendar.getInstance().getTime();
            SimpleDateFormat simpleDate = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
            String strDt = simpleDate.format(currentTime);
            Toast.makeText(getApplicationContext(), strDt, Toast.LENGTH_SHORT).show();
        }
    };
}

