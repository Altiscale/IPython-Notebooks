Set up iPython for PySpark following our documentation http://documentation.altiscale.com/using-spark-with-ipython. 

Once the iPython is set up for PySpark, do the following

cd ~/anaconda/envs/py26/bin
source activate py26
export PYSPARK_DRIVER_PYTHON=ipython
export PYSPARK_DRIVER_PYTHON_OPTS=notebook
export PYSPARK_PYTHON=python
export PYTHONPATH=/opt/spark/python/lib/py4j-0.8.2.1-src.zip:/opt/spark/python/:PYSPARK_DRIVER_PYTHON=ipython

cd $SPARK_HOME
spark_event_log_dir=$(grep 'spark.eventLog.dir' /etc/spark/spark-defaults.conf | tr -s ' ' '\t' | cut -f2)
hadoop_snappy_jar=$(find $HADOOP_HOME/share/hadoop/common/lib/ -type f -name "snappy-java-*.jar")
hadoop_lzo_jar=$(find $HADOOP_HOME/share/hadoop/common/lib/ -type f -name "hadoop-lzo-*.jar")
spark_opts_extra="$spark_opts_extra --jars $hadoop_lzo_jar,$hadoop_snappy_jar"

mkdir ~/notebooks
cd ~/notebooks  # If you have pre-existing notebooks, put them here.

/opt/spark/bin/pyspark --verbose  --name iPythondemo --conf spark.yarn.executor.memoryOverhead=2048 --conf spark.eventLog.dir=${spark_event_log_dir}$USER/ --master yarn --deploy-mode client --executor-memory 8G  --executor-cores 2 --queue default --num-executors 48 $spark_opts_extra

Now that iPython is up and running, open localhost:8888 (port as specified in ~/.ipython/profile_pyspark/ipython_notebook_config.py during set up).

Open your notebooks or make new notebooks.

The notebook PySpark_iPython_py26.ipynb makes use of a dataset about bay area bike share's trips from http://www.bayareabikeshare.com/open-data during the period from September 2014 to August 2015. The dataset is in csv. Please use csvtojson.py to convert the csv file to json file before you upload the dataset to an HDFS location.
