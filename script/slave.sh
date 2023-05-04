timedatectl
echo "gps testing"
phc_ctl /dev/ptp1 get
ptp4l -i eth0 -s &
echo "********************** Ptp4l Application is Running ***************************"
sleep 20
echo "*************** PHC clock Synchronized with Master node PHC clock***************"
phc_ctl /dev/ptp1 get
timedatectl
phc2sys -s eth0 -O 0 &
echo "********************** Phc2sys Application is Running ***************************"
sleep 5
echo "*******************  system clock Synchronized with PHC_HW ************************"
timedatectl
phc_ctl /dev/ptp1 get

