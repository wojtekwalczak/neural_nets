# neural_nets

Simple examples of neural networks.

## Auto-encoders

Currently, this repository covers a simple auto-encoder network which is able to learn a one hot vector representation for vectors of length 8 and compress the information in a three-dimensional vector.

To run the training, do:

```bash
./run.sh autoencoders/one_hot_vectors.py
```

Please, note that this script requires having Docker installed.

The result should be similar to this one:


```bash
./run.sh autoencoders/one_hot_vectors.py
0: 0.354771226644516
1: 0.3537440001964569
2: 0.35276466608047485
3: 0.35183513164520264
4: 0.35095593333244324
5: 0.35012564063072205
[...more iterations...]
49995: 1.072816724345671e-09
49996: 1.072776867339087e-09
49997: 1.0727360111317807e-09
49998: 1.0726968202590115e-09
49999: 1.0726555199624954e-09
Querying hidden layer for learned representation (encoding):
[ 1.  0.  0.  0.  0.  0.  0.  0.] => [ 1.  1.  1.]
[ 0.  1.  0.  0.  0.  0.  0.  0.] => [ 1.  1.  0.]
[ 0.  0.  1.  0.  0.  0.  0.  0.] => [ 0.  0.  0.]
[ 0.  0.  0.  1.  0.  0.  0.  0.] => [ 0.  0.  1.]
[ 0.  0.  0.  0.  1.  0.  0.  0.] => [ 1.  0.  0.]
[ 0.  0.  0.  0.  0.  1.  0.  0.] => [ 0.  1.  1.]
[ 0.  0.  0.  0.  0.  0.  1.  0.] => [ 0.  1.  0.]
[ 0.  0.  0.  0.  0.  0.  0.  1.] => [ 1.  0.  1.]

Querying output layer (decoding):
[ 1.  1.  1.] => [ 1.  0.  0.  0.  0.  0.  0.  0.]
[ 1.  1.  0.] => [ 0.  1.  0.  0.  0.  0.  0.  0.]
[ 0.  0.  0.] => [ 0.  0.  1.  0.  0.  0.  0.  0.]
[ 0.  0.  1.] => [ 0.  0.  0.  1.  0.  0.  0.  0.]
[ 1.  0.  0.] => [ 0.  0.  0.  0.  1.  0.  0.  0.]
[ 0.  1.  1.] => [ 0.  0.  0.  0.  0.  1.  0.  0.]
[ 0.  1.  0.] => [ 0.  0.  0.  0.  0.  0.  1.  0.]
[ 1.  0.  1.] => [ 0.  0.  0.  0.  0.  0.  0.  1.]
```

