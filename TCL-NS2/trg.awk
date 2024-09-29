awk '{
    if ($1 == "r" && $4 == "tcp") {
        received_bytes += $6
    }
}
END {
    print "Throughput: " received_bytes / (300 * 1024 * 1024) " Mbps"
}' out_reno.tr
