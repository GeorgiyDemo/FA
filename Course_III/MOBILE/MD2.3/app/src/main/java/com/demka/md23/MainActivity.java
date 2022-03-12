package com.demka.md23;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private static final int CAMERA_REQUEST = 1888;
    ImageView mainImageView;
    Button cameraButton;
    Button mainTaskButton;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainImageView = findViewById(R.id.mainImageView);
        cameraButton = findViewById(R.id.cameraButton);
        mainTaskButton = findViewById(R.id.mainTaskButton);

        View.OnClickListener mainTaskButtonListener = this::mainTaskButtonClicked;
        View.OnClickListener cameraButtonListener = this::cameraButtonClicked;
        cameraButton.setOnClickListener(cameraButtonListener);
        mainTaskButton.setOnClickListener(mainTaskButtonListener);
    }

    public void mainTaskButtonClicked(View v) {
        Intent intent = new Intent(this, TODOCategoriesActivity.class);
        startActivity(intent);
    }

    public void cameraButtonClicked(View v) {
        Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(cameraIntent, CAMERA_REQUEST);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == CAMERA_REQUEST && resultCode == Activity.RESULT_OK) {
            Bitmap photo = (Bitmap) data.getExtras().get("data");
            mainImageView.setImageBitmap(photo);
        }
    }
}