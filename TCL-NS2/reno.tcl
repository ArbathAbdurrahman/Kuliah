# Define a simulator object
set ns [new Simulator]

# Open the nam trace file
set nf [open out.nam w]
$ns namtrace-all $nf

# Open the trace file
set tf [open out.tr w]
$ns trace-all $tf

# Define a finish procedure
proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam out.nam &
    exit 0
}

# Create nodes
set n0 [$ns node]
set n1 [$ns node]

# Create a duplex link between the nodes
$ns duplex-link $n0 $n1 1Mb 10ms DropTail

# Set the TCP source and sink
set tcp [new Agent/TCP/Reno]
$tcp set class_ 2
$ns attach-agent $n0 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink
$ns connect $tcp $sink

# Create a CBR traffic generator
set cbr [new Application/Traffic/CBR]
$cbr set packet_size_ 500
$cbr set rate_ 1Mb
$cbr attach-agent $tcp

# Schedule events
$ns at 0.1 "$cbr start"
$ns at 4.5 "$cbr stop"
$ns at 5.0 "finish"

# Run the simulation
$ns run
