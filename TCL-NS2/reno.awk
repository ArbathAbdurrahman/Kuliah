awk '{
    if ($1 == "r" && $4 == "tcp") received++;
    if ($1 == "s" && $4 == "tcp") sent++;
}
END {
    print "Packets Sent: " sent;
    print "Packets Received: " received;
}' out.tr
