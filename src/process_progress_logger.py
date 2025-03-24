import sys
import time
from typing import Callable, Optional, Any


class ProcessProgressLogger:
    """
    A utility class to log real-time progress of a process.
    
    Supports updating progress with percentage, current stage, 
    and custom logging callback.
    """
    
    def __init__(
        self, 
        total_steps: int, 
        update_interval: float = 0.5, 
        log_callback: Optional[Callable[[str], None]] = None
    ):
        """
        Initialize the progress logger.
        
        Args:
            total_steps (int): Total number of steps in the process
            update_interval (float, optional): Minimum time between progress updates. Defaults to 0.5 seconds.
            log_callback (Callable, optional): Custom logging function. Defaults to sys.stdout write.
        
        Raises:
            ValueError: If total_steps is not a positive integer
        """
        if not isinstance(total_steps, int) or total_steps <= 0:
            raise ValueError("total_steps must be a positive integer")
        
        self.total_steps = total_steps
        self.current_step = 0
        self.update_interval = update_interval
        self.last_update_time = 0
        
        # Use provided log callback or default to print to stdout
        self.log_callback = log_callback or (lambda msg: print(msg, flush=True))
    
    def update(self, steps_completed: int = 1) -> None:
        """
        Update the progress of the process.
        
        Args:
            steps_completed (int, optional): Number of steps completed. Defaults to 1.
        
        Raises:
            ValueError: If steps_completed is negative
            ValueError: If total progress would exceed total steps
        """
        if steps_completed < 0:
            raise ValueError("Steps completed cannot be negative")
        
        current_time = time.time()
        
        # Update current step
        self.current_step = min(self.current_step + steps_completed, self.total_steps)
        
        # Check if enough time has passed since last update
        if current_time - self.last_update_time >= self.update_interval:
            # Calculate percentage
            percentage = (self.current_step / self.total_steps) * 100
            
            # Format progress message
            progress_msg = f"Progress: {self.current_step}/{self.total_steps} steps " \
                           f"({percentage:.2f}%)"
            
            # Log the progress
            self.log_callback(progress_msg)
            
            # Update last update time
            self.last_update_time = current_time
    
    def complete(self) -> None:
        """
        Mark the process as complete, ensuring final 100% update.
        """
        if self.current_step < self.total_steps:
            self.current_step = self.total_steps
            self.log_callback(f"Progress: {self.total_steps}/{self.total_steps} steps (100.00%)")
    
    def __enter__(self):
        """
        Support context manager protocol for easy use.
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ensure completion when exiting context.
        """
        if exc_type is None:
            self.complete()