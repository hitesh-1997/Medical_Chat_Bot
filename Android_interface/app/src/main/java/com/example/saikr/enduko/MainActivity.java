package com.example.saikr.enduko;

import android.annotation.TargetApi;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.speech.RecognizerIntent;
import android.speech.tts.TextToSpeech;
import android.speech.tts.UtteranceProgressListener;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    private static final String DEBUG_TAG = "HttpExample";
    private EditText urlText;
    private TextView textView;
    private Button button;
    private Button chitti;
    private int[] arr;
    private String output;
    private int qIndex;
    AlertDialog alertDialog;
    AlertDialog.Builder builder;
    private TextView txtSpeechInput;
    private ImageButton btnSpeak;
    private final int REQ_CODE_SPEECH_INPUT = 100;
    private  int olm=1;
    TextToSpeech t1;
    static final int USER_LOGIN_REQUEST = 1;

    // @Sodhi add code to fetch the user id
    private String user_id = "hello";
    private  CheckBox hindiCheck;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        arr=new int[19];
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        urlText = (EditText) findViewById(R.id.myUrl);
        textView = (TextView) findViewById(R.id.myText);
        button=(Button)findViewById(R.id.but);
        chitti=(Button)findViewById(R.id.bt2);
        txtSpeechInput = (TextView) findViewById(R.id.txtSpeechInput);
        btnSpeak = (ImageButton) findViewById(R.id.btnSpeak);
        hindiCheck = (CheckBox) findViewById(R.id.hindi);

        btnSpeak.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                promptSpeechInput();
            }
        });
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Toast.makeText(getApplicationContext(),"hai "+arr[15],Toast.LENGTH_LONG).show();
                String sturl = "http://medapp.pythonanywhere.com/webapp/first?";
                String stringUrl = urlText.getText().toString();
                stringUrl = stringUrl.replaceAll(" ", "_");
                sturl = sturl.concat(stringUrl);
                stringUrl = sturl.concat("#");
                myClickHandler(v, stringUrl);
                urlText.setText("");
            }
        });

        chitti.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(olm==1){
                    olm=0;
                    ViewGroup layout = (ViewGroup) button.getParent();
                    if(null!=layout) //for safety only  as you are doing onClick
                        layout.removeView(button);
                }
                if(qIndex>0){
                    String answer=urlText.getText().toString();
                    Log.d("Input:",answer);

                    if(answer.equalsIgnoreCase("yes") || answer.equalsIgnoreCase("हां"))
                    {
                        arr[qIndex]=1;
                    }
                    else if(answer.equalsIgnoreCase("no") || answer.equalsIgnoreCase("नहीं")){
                        arr[qIndex]=2;
                    }
                    else{
                        if(!hindiCheck.isChecked())
                            Toast.makeText(getApplicationContext(),"Please enter your answer (yes/no)",Toast.LENGTH_LONG).show();
                        else
                            Toast.makeText(getApplicationContext(), "अपना जवाब हाँ या नही में दे", Toast.LENGTH_LONG).show();
                        return;
                    }
                    qIndex=0;
                }
                String sturl="http://medapp.pythonanywhere.com/webapp/second?";
                sturl=sturl.concat(Arrays.toString(arr));
                sturl=sturl.concat("#");
                sturl=sturl.replaceAll("\\[","");
                sturl=sturl.replaceAll("\\]","");
                sturl=sturl.replaceAll(" ","");
                //Toast.makeText(getApplicationContext(),"output "+sturl,Toast.LENGTH_LONG).show();
                Toast.makeText(getApplicationContext(),"Submitting...", Toast.LENGTH_LONG).show();
                myClickHandler(v, sturl);
            }
        });




        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        boolean logged_in = sharedPreferences.getBoolean("logged_in", false);

        if (logged_in) {
            user_id = sharedPreferences.getString("user_id", "sodhi123");
        } else {
            Intent intent = new Intent(MainActivity.this, LoginActivity.class);
            startActivityForResult(intent, USER_LOGIN_REQUEST);
        }

    }

    public void onPause(){
        if(t1 !=null){
            t1.stop();
            t1.shutdown();
        }
        super.onPause();
    }


    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);

        if(!hindiCheck.isChecked()){
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                    RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        }

        else
        {
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, "hi_IN");
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "hi_IN");
        }

        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                getString(R.string.speech_prompt));
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    getString(R.string.speech_not_supported),
                    Toast.LENGTH_SHORT).show();
        }
    }

    /**
     * Receiving speech input
     * */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    urlText.setText(result.get(0));
                    chitti.performClick();
                }
                break;
            }
            case USER_LOGIN_REQUEST: {
                user_id = data.getStringExtra("user_id");

                // saving that a user has now been logged in
                SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this);
                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putBoolean("logged_in", true);
                editor.putString("user_id", user_id);

                editor.commit();

                Log.d("LOGIN", "Logged in, user_id: " + user_id);
                break;
            }
        }
    }
    private void updateSymptoms() {
        Context context  = getApplicationContext();
        String intrm = output.substring(0,1);
        //Toast.makeText(getApplicationContext(),output,Toast.LENGTH_LONG).show();
        if(!intrm.equals("[")){
            builder=new AlertDialog.Builder(this);
            builder.setTitle("Disease");
            builder.setMessage(output);
            builder.setPositiveButton("Ok", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    Intent i = getBaseContext().getPackageManager()
                            .getLaunchIntentForPackage(getBaseContext().getPackageName());
                    i.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                    startActivity(i);
                }
            });
            builder.setNegativeButton("Exit", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    System.exit(0);
                }
            });
            builder.setNeutralButton("Map", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    Intent i=new Intent(MainActivity.this,MapsActivity.class);
                    startActivity(i);
                }
            });
            alertDialog=builder.create();
            alertDialog.show();

            }
        else {
            int i = -1;
            output = output.replaceAll(" ", "");
            //Toast.makeText(getApplicationContext(),"lolll ",Toast.LENGTH_LONG).show();
            for (i = 0; i < 19; i++) {
                int b = Integer.parseInt(output.substring((2 * i) + 1, (2 * i) + 2));
                if (b != 0) {
                    arr[i] = b;
                    if (b == 2) {
                        qIndex = i;
                        askQuestion();
                        //Toast.makeText(getApplicationContext(),"zzzzz ",Toast.LENGTH_LONG).show();
                    }
                }
            }
            //Toast.makeText(getApplicationContext(),"hello "+arr,Toast.LENGTH_LONG).show();
        }

    }

    private void askQuestion() {





        //Toast.makeText(getApplicationContext(),"uuuuuuu ",Toast.LENGTH_LONG).show();
        int temp = qIndex;

        String help = "";

        if(!hindiCheck.isChecked()){
            if ( temp == 1)
                help = ("Have you been experiencing headache (yes/no)");
            else if ( temp == 2)
                help = ("Have you been experiencing vomit (yes/no)");
            else if ( temp == 3)
                help = ("Have you been experiencing nausea (yes/no)");
            else if ( temp == 4)
                help = ("Have you been experiencing pain in eye (yes/no)");
            else if ( temp == 5)
                help = ("Have you been experiencing pain in muscle (yes/no)");
            else if ( temp == 6)
                help = ("Have you been experiencing pain in chest (yes/no)");
            else if ( temp == 7)
                help = ("Have you been experiencing chills or high spike in fever (yes/no)");
            else if ( temp == 8)
                help = ("Have you been experiencing pain in nerve (yes/no)");
            else if ( temp == 9)
                help = ("Have you been experiencing pain in joint (yes/no)");
            else if ( temp == 10)
                help = ("Have you been experiencing bleeding gums (yes/no)");
            else if ( temp == 11)
                help = ("Have you been experiencing itching  (yes/no)");
            else if ( temp == 12)
                help = ("Are there any rashes occuring (yes/no)");
            else if ( temp == 13)
                help = ("Have you been experiencing fever (yes/no)");
            else if ( temp == 14)
                help = ("Have you been experiencing abdominal pain or stomach ache (yes/no)");
            else if ( temp == 15)
                help = ("Have you been experiencing diarrhea (yes/no)");
            else if ( temp == 16)
                help = ("Have you been experiencing dizziness (yes/no)");
            else if ( temp == 17)
                help = ("Have you been experiencing discomfort (yes/no)");
            else if ( temp == 18)
                help = ("Have you been experiencing bleeding nose (yes/no)");
        }
        else {
                if (temp == 1)
                    help = ("क्या आपके सर में दर्द हो रहा है, हाँ या नही में जवाब दें");
                else if (temp == 2)
                    help = ("क्या आपको उल्टियाँ आ रही हें, हाँ या नही में जवाब दें");
                else if (temp == 3)
                    help = ("क्या आपको मतली हो रही हे, हाँ या नही में जवाब दें");
                else if (temp == 4)
                    help = ("क्या आपके आँख में दर्द हे, हाँ या नही में जवाब दें");
                else if (temp == 5)
                    help = ("क्या आपकी मसपेसिओं में दर्द हे, हाँ या नही में जवाब दें");
                else if (temp == 6)
                    help = ("क्या आपके छाती में दर्द हो रा हे, हाँ या नही में जवाब दें");
                else if (temp == 7)
                    help = ("क्या आपका बुखार हाल ही में बढ़ा हे या फिर आप काप रहे हें, हाँ या नही में जवाब दें");
                else if (temp == 8)
                    help = ("क्या आपके नस में दर्द हे, हाँ या नही में जवाब दें");
                else if (temp == 9)
                    help = ("क्या आपके जोड़ों में दर्द हे, हाँ या नही में जवाब दें");
                else if (temp == 10)
                    help = ("क्या आपके मसूड़ों में खून हे, हाँ या नही में जवाब दें");
                else if (temp == 11)
                    help = ("क्या आपको खुजली हे, हाँ या नही में जवाब दें");
                else if (temp == 12)
                    help = ("क्या आपको चकते हे, हाँ या नही में जवाब दें");
                else if (temp == 13)
                    help = ("क्या आपको बुखार हे, हाँ या नही में जवाब दें");
                else if (temp == 14)
                    help = ("क्या आपको पेट में दर्द हे, हाँ या नही में जवाब दें");
                else if (temp == 15)
                    help = ("क्या आपको डायरिया हे, हाँ या नही में जवाब दें");
                else if (temp == 16)
                    help = ("क्या आपको चक्कर हे, हाँ या नही में जवाब दें");
                else if (temp == 17)
                    help = ("क्या आपको तकलीफ़ हे, हाँ या नही में जवाब दें");
                else if (temp == 18)
                    help = ("क्या आपके नाक से खून निकल रा हे, हाँ या नही में जवाब दें");
            }

        textView.setText(help);
        Toast.makeText(getApplicationContext(),help, Toast.LENGTH_LONG).show();

        t1=new TextToSpeech(getApplicationContext(), new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {

                if(status != TextToSpeech.ERROR) {
                    if(!hindiCheck.isChecked())
                        t1.setLanguage(Locale.ENGLISH);
                    else
                        t1.setLanguage(new Locale("hi", "IN"));
                    t1.setOnUtteranceProgressListener(new UtteranceProgressListener() {
                        @Override
                        public void onStart(String s) {

                        }

                        @Override
                        public void onDone(String s) {
                            MainActivity.this.runOnUiThread(new Runnable() {
                                @Override
                                public void run() {
                                    btnSpeak.performClick();
                                }
                            });
                        }

                        @Override
                        public void onError(String s) {

                        }
                    });

                }
                else {
                    Log.e("MainActivity", "Initilization Failed!");
                }

                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
                    ttsGreater21(String.valueOf(textView.getText()));
                } else {
                    ttsUnder20(String.valueOf(textView.getText()));
                }

            }
        });


        urlText.setText("");

    }


    @SuppressWarnings("deprecation")
    private void ttsUnder20(String string) {
        HashMap<String, String> map = new HashMap<>();
        map.put(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, "MessageId");
        t1.speak(string, TextToSpeech.QUEUE_FLUSH, map);
    }

    @TargetApi(Build.VERSION_CODES.LOLLIPOP)
    private void ttsGreater21(String string) {
        String utteranceId=this.hashCode() + "";
        t1.speak(string, TextToSpeech.QUEUE_FLUSH, null, utteranceId);
    }

    public void myClickHandler(View view,String sturl) {
        // Gets the URL from the UI's text field.

        //Toast.makeText(getApplicationContext(),stringUrl,Toast.LENGTH_LONG).show();
        //Toast.makeText(getApplicationContext(),stringUrl+' '+sturl,Toast.LENGTH_LONG).show();
        ConnectivityManager connMgr = (ConnectivityManager)
                getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
        if (networkInfo != null && networkInfo.isConnected()) {
            new DownloadWebpageTask().execute(sturl);
        } else {
            textView.setText("No network connection available.");
        }
    }

    // Uses AsyncTask to create a task away from the main UI thread. This task takes a
    // URL string and uses it to create an HttpUrlConnection. Once the connection
    // has been established, the AsyncTask downloads the contents of the webpage as
    // an InputStream. Finally, the InputStream is converted into a string, which is
    // displayed in the UI by the AsyncTask's onPostExecute method.
    private class DownloadWebpageTask extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... urls) {

            // params comes from the execute() call: params[0] is the url.
            try {
                return downloadUrl(urls[0]);
            } catch (IOException e) {
                return "Unable to retrieve web page. URL may be invalid.";
            }
        }


        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {

            output=result;
            //Toast.makeText(getApplicationContext(),"output2 "+output,Toast.LENGTH_LONG).show();
            updateSymptoms();
            //textView.setText(Arrays.toString(arr));
        }
    }
    // Given a URL, establishes an HttpUrlConnection and retrieves
// the web page content as a InputStream, which it returns as
// a string.
    private String downloadUrl(String myurl) throws IOException {
        InputStream is = null;
        // Only display the first 500 characters of the retrieved
        // web page content.
        int len = 500;

        try {
            URL url = new URL(myurl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setReadTimeout(10000 /* milliseconds */);
            conn.setConnectTimeout(15000 /* milliseconds */);
            conn.setRequestMethod("GET");
            conn.setDoInput(true);

            conn.addRequestProperty("userId", user_id);
            // Starts the query
            conn.connect();
            int response = conn.getResponseCode();
            Log.d(DEBUG_TAG, "The response is: " + response);
            is = conn.getInputStream();

            // Convert the InputStream into a string
            String contentAsString = readIt(is, len);
            return contentAsString;

            // Makes sure that the InputStream is closed after the app is
            // finished using it.
        } finally {
            if (is != null) {
                is.close();
            }
        }
    }
    public String readIt(InputStream stream, int len) throws IOException, UnsupportedEncodingException {
        Reader reader = null;
        reader = new InputStreamReader(stream, "UTF-8");
        char[] buffer = new char[len];
        reader.read(buffer);
        return new String(buffer);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.disease_history) {
            Intent intent = new Intent(MainActivity.this, DiseaseHistory.class);
            intent.putExtra("user_id", user_id);
            startActivity(intent);
        }

        return super.onOptionsItemSelected(item);
    }
}
