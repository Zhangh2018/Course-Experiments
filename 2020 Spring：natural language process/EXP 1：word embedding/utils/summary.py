from tensorboardX import SummaryWriter
import os

def mkdirs(newdir):

	try:
		if not os.path.exists(newdir):
			os.makedirs(newdir)
	except OSError as err:
		if err.errno != errno.EEXIST or not os.path.isdir(newdir):
			raise


class LogSummary(object):

	def __init__(self, log_path):

		mkdirs(log_path)
		self.writer = SummaryWriter(log_path)


	def write_scalars(self, scalar_dict, n_iter, tag=None):

		for name, scalar in scalar_dict.items():
			if tag is not None:
				name = '/'.join([tag, name])
			self.writer.add_scalar(name, scalar, n_iter)


	def write_hist_parameters(self, net, n_iter):
		for name, param in net.named_parameters():
			self.writer.add_histogram(name, param.clone().cpu().numpy(), n_iter)
