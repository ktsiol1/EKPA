{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJEZ6aiB6ZZoBd78JL0I69",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ktsiol1/EKPA/blob/main/IDS.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gbqvS-UIKS3T",
        "outputId": "a8bc14ae-425c-4b07-ac96-3e813ac864da"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Κατανομή κλάσεων y:\n",
            "target\n",
            "1    396743\n",
            "0     97278\n",
            "Name: count, dtype: int64\n",
            "Blocking 118365 malicious traffic instances.\n",
            "Epoch 1, Iteration 10000, Test Accuracy: 0.9956142422422692\n",
            "Blocking 118176 malicious traffic instances.\n",
            "Epoch 1, Iteration 20000, Test Accuracy: 0.9943389988327137\n",
            "Blocking 118346 malicious traffic instances.\n",
            "Epoch 1, Iteration 30000, Test Accuracy: 0.995486043169351\n",
            "Blocking 118411 malicious traffic instances.\n",
            "Epoch 1, Iteration 40000, Test Accuracy: 0.9959246189451241\n",
            "Blocking 118430 malicious traffic instances.\n",
            "Epoch 1, Iteration 50000, Test Accuracy: 0.9960528180180424\n",
            "Blocking 118123 malicious traffic instances.\n",
            "Epoch 1, Iteration 60000, Test Accuracy: 0.993981390892468\n",
            "Blocking 118120 malicious traffic instances.\n",
            "Epoch 1, Iteration 70000, Test Accuracy: 0.9939611489335861\n",
            "Blocking 118419 malicious traffic instances.\n",
            "Epoch 1, Iteration 80000, Test Accuracy: 0.9959785975021422\n",
            "Blocking 118277 malicious traffic instances.\n",
            "Epoch 1, Iteration 90000, Test Accuracy: 0.9950204781150688\n",
            "Blocking 118267 malicious traffic instances.\n",
            "Epoch 1, Iteration 100000, Test Accuracy: 0.994953004918796\n",
            "Blocking 118334 malicious traffic instances.\n",
            "Epoch 1, Iteration 110000, Test Accuracy: 0.9954050753338236\n",
            "Blocking 118337 malicious traffic instances.\n",
            "Epoch 1, Iteration 120000, Test Accuracy: 0.9954253172927054\n",
            "Blocking 118273 malicious traffic instances.\n",
            "Epoch 1, Iteration 130000, Test Accuracy: 0.9949934888365597\n",
            "Blocking 118409 malicious traffic instances.\n",
            "Epoch 1, Iteration 140000, Test Accuracy: 0.9959111243058695\n",
            "Blocking 118302 malicious traffic instances.\n",
            "Epoch 1, Iteration 150000, Test Accuracy: 0.9951891611057507\n",
            "Blocking 118254 malicious traffic instances.\n",
            "Epoch 1, Iteration 160000, Test Accuracy: 0.9948652897636414\n",
            "Blocking 118334 malicious traffic instances.\n",
            "Epoch 1, Iteration 170000, Test Accuracy: 0.9954050753338236\n",
            "Blocking 118268 malicious traffic instances.\n",
            "Epoch 1, Iteration 180000, Test Accuracy: 0.9949597522384233\n",
            "Blocking 118393 malicious traffic instances.\n",
            "Epoch 1, Iteration 190000, Test Accuracy: 0.995803167191833\n",
            "Blocking 118392 malicious traffic instances.\n",
            "Epoch 1, Iteration 200000, Test Accuracy: 0.9957964198722058\n",
            "Blocking 118395 malicious traffic instances.\n",
            "Epoch 1, Iteration 210000, Test Accuracy: 0.9958166618310876\n",
            "Blocking 118251 malicious traffic instances.\n",
            "Epoch 1, Iteration 220000, Test Accuracy: 0.9948450478047596\n",
            "Blocking 118348 malicious traffic instances.\n",
            "Epoch 1, Iteration 230000, Test Accuracy: 0.9954995378086056\n",
            "Blocking 118202 malicious traffic instances.\n",
            "Epoch 1, Iteration 240000, Test Accuracy: 0.9945144291430229\n",
            "Blocking 118303 malicious traffic instances.\n",
            "Epoch 1, Iteration 250000, Test Accuracy: 0.995195908425378\n",
            "Blocking 118263 malicious traffic instances.\n",
            "Epoch 1, Iteration 260000, Test Accuracy: 0.9949260156402869\n",
            "Blocking 118314 malicious traffic instances.\n",
            "Epoch 1, Iteration 270000, Test Accuracy: 0.9952701289412781\n",
            "Blocking 118216 malicious traffic instances.\n",
            "Epoch 1, Iteration 280000, Test Accuracy: 0.9946088916178049\n",
            "Blocking 118342 malicious traffic instances.\n",
            "Epoch 1, Iteration 290000, Test Accuracy: 0.9954590538908419\n",
            "Blocking 118498 malicious traffic instances.\n",
            "Epoch 1, Iteration 300000, Test Accuracy: 0.9965116357526972\n",
            "Blocking 118353 malicious traffic instances.\n",
            "Epoch 1, Iteration 310000, Test Accuracy: 0.9955332744067419\n",
            "Blocking 118226 malicious traffic instances.\n",
            "Epoch 1, Iteration 320000, Test Accuracy: 0.9946763648140776\n",
            "Blocking 118413 malicious traffic instances.\n",
            "Epoch 1, Iteration 330000, Test Accuracy: 0.9959381135843786\n",
            "Blocking 118160 malicious traffic instances.\n",
            "Epoch 1, Iteration 340000, Test Accuracy: 0.9942310417186773\n",
            "Blocking 118365 malicious traffic instances.\n",
            "Epoch 2, Iteration 10000, Test Accuracy: 0.9956142422422692\n",
            "Blocking 118176 malicious traffic instances.\n",
            "Epoch 2, Iteration 20000, Test Accuracy: 0.9943389988327137\n",
            "Blocking 118346 malicious traffic instances.\n",
            "Epoch 2, Iteration 30000, Test Accuracy: 0.995486043169351\n",
            "Blocking 118411 malicious traffic instances.\n",
            "Epoch 2, Iteration 40000, Test Accuracy: 0.9959246189451241\n",
            "Blocking 118430 malicious traffic instances.\n",
            "Epoch 2, Iteration 50000, Test Accuracy: 0.9960528180180424\n",
            "Blocking 118123 malicious traffic instances.\n",
            "Epoch 2, Iteration 60000, Test Accuracy: 0.993981390892468\n",
            "Blocking 118120 malicious traffic instances.\n",
            "Epoch 2, Iteration 70000, Test Accuracy: 0.9939611489335861\n",
            "Blocking 118419 malicious traffic instances.\n",
            "Epoch 2, Iteration 80000, Test Accuracy: 0.9959785975021422\n",
            "Blocking 118277 malicious traffic instances.\n",
            "Epoch 2, Iteration 90000, Test Accuracy: 0.9950204781150688\n",
            "Blocking 118267 malicious traffic instances.\n",
            "Epoch 2, Iteration 100000, Test Accuracy: 0.994953004918796\n",
            "Blocking 118334 malicious traffic instances.\n",
            "Epoch 2, Iteration 110000, Test Accuracy: 0.9954050753338236\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report\n",
        "from imblearn.over_sampling import SMOTENC\n",
        "from imblearn.pipeline import Pipeline as ImbPipeline\n",
        "from sklearn.compose import ColumnTransformer\n",
        "import requests\n",
        "from io import BytesIO\n",
        "import gzip\n",
        "import numpy as np\n",
        "\n",
        "# Κατέβασμα και αποσυμπίεση του συνόλου δεδομένων KDD Cup 1999\n",
        "url = \"http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz\"\n",
        "response = requests.get(url, stream=True)\n",
        "compressed_file = BytesIO(response.content)\n",
        "decompressed_file = gzip.GzipFile(fileobj=compressed_file)\n",
        "\n",
        "# Φόρτωση του dataset\n",
        "columns = [\"duration\", \"protocol_type\", \"service\", \"flag\", \"src_bytes\", \"dst_bytes\", \"land\",\n",
        "           \"wrong_fragment\", \"urgent\", \"hot\", \"num_failed_logins\", \"logged_in\", \"num_compromised\",\n",
        "           \"root_shell\", \"su_attempted\", \"num_root\", \"num_file_creations\", \"num_shells\",\n",
        "           \"num_access_files\", \"num_outbound_cmds\", \"is_host_login\", \"is_guest_login\",\n",
        "           \"count\", \"srv_count\", \"serror_rate\", \"srv_serror_rate\", \"rerror_rate\", \"srv_rerror_rate\",\n",
        "           \"same_srv_rate\", \"diff_srv_rate\", \"srv_diff_host_rate\", \"dst_host_count\",\n",
        "           \"dst_host_srv_count\", \"dst_host_same_srv_rate\", \"dst_host_diff_srv_rate\",\n",
        "           \"dst_host_same_src_port_rate\", \"dst_host_srv_diff_host_rate\", \"dst_host_serror_rate\",\n",
        "           \"dst_host_srv_serror_rate\", \"dst_host_rerror_rate\", \"dst_host_srv_rerror_rate\", \"target\"]\n",
        "df = pd.read_csv(decompressed_file, header=None, names=columns)\n",
        "\n",
        "# Δημιουργία του συνόλου σε δύο κλάσεις Normal (0) και Attack (1)\n",
        "X = df.drop(\"target\", axis=1)\n",
        "y = df[\"target\"].apply(lambda x: 0 if x == \"normal.\" else 1)\n",
        "\n",
        "# Έλεγχος κατηγοριών\n",
        "print(\"Κατανομή κλάσεων y:\")\n",
        "print(y.value_counts())\n",
        "\n",
        "# Εντοπισμός κατηγορικών μεταβλητών\n",
        "categorical_features = ['protocol_type', 'service', 'flag']\n",
        "\n",
        "# Διαχωρισμός κατηγορικών και αριθμητικών μεταβλητών\n",
        "numeric_features = X.columns.difference(categorical_features)\n",
        "\n",
        "# Δημιουργία διοχέτευσης (αγωγού) προεπεξεργασίας με κωδικοποίηση μίας δέσμης (one-hot encoding) για κατηγορικές μεταβλητές\n",
        "preprocessor = ColumnTransformer(\n",
        "    transformers=[\n",
        "        ('num', StandardScaler(), numeric_features),\n",
        "        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)\n",
        "    ])\n",
        "\n",
        "# Τμηματοποίηση δεδομένων σε σύνολα εκπαίδευσης και δοκιμών\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
        "\n",
        "# Δημιουργία διοχέτευσης (αγωγού) SMOTE για τις αριθμητικές μεταβλητές μόνο\n",
        "pipeline = ImbPipeline([\n",
        "    ('preprocessor', preprocessor),\n",
        "    ('smote', SMOTENC(random_state=42, categorical_features=[X.columns.get_loc(col) for col in categorical_features])),\n",
        "    ('classifier', RandomForestClassifier(random_state=42))\n",
        "])\n",
        "\n",
        "# Καθορισμός κατωφλίου (threshold) για την διακοπή διακτυακής κίνησης\n",
        "blocking_threshold = 0.9\n",
        "\n",
        "# Δημιουργία ενημερωμένου βρόχου συνεχούς - αυξητικής μάθησης\n",
        "batch_size = 10000\n",
        "for epoch in range(1, 3):\n",
        "    for i in range(0, len(X_train), batch_size):\n",
        "        X_batch = X_train.iloc[i:i + batch_size]\n",
        "        y_batch = y_train.iloc[i:i + batch_size]\n",
        "\n",
        "        # Σταδιακή ενημέρωση του μοντέλου με κάθε ροή (batch) δεδομένων\n",
        "        pipeline.fit(X_batch, y_batch)\n",
        "\n",
        "        # Περιοδική ενημέρωση του μοντέλου στ\n",
        "        if i % batch_size == 0 and i > 0:\n",
        "            y_pred_proba = pipeline.predict_proba(X_test)[:, 1]\n",
        "\n",
        "            # Αποκλεισμός δικτυακής κυκλοφορίας εάν η προβλεπόμενη πιθανότητα υπερβαίνει το καθορισμένο όριο\n",
        "            blocked_indices = np.where(y_pred_proba > blocking_threshold)[0]\n",
        "            if len(blocked_indices) > 0:\n",
        "                print(f\"Blocking {len(blocked_indices)} malicious traffic instances.\")\n",
        "\n",
        "            accuracy = accuracy_score(y_test, y_pred_proba > blocking_threshold)\n",
        "            print(f\"Epoch {epoch}, Iteration {i}, Test Accuracy: {accuracy}\")\n",
        "\n",
        "# Τελική αξιολόγηση του μοντέλου στο σύνολο δοκιμών\n",
        "y_pred_proba = pipeline.predict_proba(X_test)[:, 1]\n",
        "blocked_indices = np.where(y_pred_proba > blocking_threshold)[0]\n",
        "if len(blocked_indices) > 0:\n",
        "    print(f\"Blocking {len(blocked_indices)} malicious traffic instances.\")\n",
        "\n",
        "accuracy = accuracy_score(y_test, y_pred_proba > blocking_threshold)\n",
        "classification_rep = classification_report(y_test, y_pred_proba > blocking_threshold)\n",
        "\n",
        "# Εκτύπωση τελικών αποτελεσμάτων\n",
        "print(f\"Final Test Accuracy: {accuracy}\")\n",
        "print(\"Classification Report:\")\n",
        "print(classification_rep)\n"
      ]
    }
  ]
}