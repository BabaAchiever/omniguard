import psutil
import ctypes
import time
import logging

# Set up logging
logging.basicConfig(filename='omniguard.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def bytes_to_mb(bytes_value):
    """Convert bytes to megabytes."""
    return bytes_value / (1024 ** 2)

def optimize_memory():
    """Optimize memory usage by freeing up RAM."""
    try:
        # Get the current memory usage
        memory_info = psutil.virtual_memory()
        available_memory = bytes_to_mb(memory_info.available)
        total_memory = bytes_to_mb(memory_info.total)

        logging.info(f"Available Memory: {available_memory:.2f} MB / Total Memory: {total_memory:.2f} MB")

        # Check if the available memory is less than 20% of total memory
        if available_memory / total_memory < 0.2:
            logging.info("Memory usage is high, attempting to optimize memory.")
            # Call Windows API to empty the working sets of all processes
            ctypes.windll.psapi.EmptyWorkingSet(-1)
            logging.info("Memory optimization complete.")
        else:
            logging.info("Memory usage is within acceptable limits. No optimization needed.")
    except Exception as e:
        logging.error(f"Error during memory optimization: {e}")

def main():
    """Main function to periodically optimize memory."""
    logging.info("OmniGuard started.")
    while True:
        optimize_memory()
        time.sleep(60)  # Run every 60 seconds

if __name__ == "__main__":
    main()